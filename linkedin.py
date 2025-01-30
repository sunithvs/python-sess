import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime


def get_job_listings(num_pages=5):
    jobs_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for page in range(num_pages):
        try:
            # Construct URL for Python jobs in Kochi
            url = f'https://www.linkedin.com/jobs/search?keywords=Python&location=Kochi%2C%20Kerala%2C%20India&geoId=105307040&f_TP=1%2C2&start={page * 25}'

            # Make request
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all job cards
            job_cards = soup.find_all('div', class_='base-card')

            # If no jobs found on page, break
            if not job_cards:
                break

            # Extract information from each job card
            for card in job_cards:
                try:
                    title = card.find('h3', class_='base-search-card__title').text.strip()
                    company = card.find('h4', class_='base-search-card__subtitle').text.strip()
                    location = card.find('span', class_='job-search-card__location').text.strip()
                    link = card.find('a', class_='base-card__full-link').get('href')

                    try:
                        posted_time = card.find('time', class_='job-search-card__listdate').text.strip()
                    except:
                        posted_time = "N/A"

                    try:
                        description = card.find('p', class_='base-search-card__metadata').text.strip()
                    except:
                        description = "N/A"
                    jobs_list.append({
                        'Title': title,
                        'Company': company,
                        'Location': location,
                        'Posted': posted_time,
                        'Description': description,
                        'Link': link
                    })

                except Exception as e:
                    print(f"Error processing job card: {e}")
                    continue

            # Add delay to avoid rate limiting
            time.sleep(2)

        except Exception as e:
            print(f"Error processing page {page}: {e}")
            continue

    return jobs_list


def save_to_csv(jobs):
    # Create DataFrame
    df = pd.DataFrame(jobs)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'python_jobs_kochi_{timestamp}.csv'

    # Save to CSV
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"Jobs saved to {filename}")
    print(f"Total jobs found: {len(jobs)}")


def main():
    print("Scraping LinkedIn for Python jobs in Kochi...")
    jobs = get_job_listings()

    if jobs:
        save_to_csv(jobs)
    else:
        print("No jobs found!")


if __name__ == "__main__":
    main()
