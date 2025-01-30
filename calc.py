def calculator():
    """
    A basic calculator that handles addition, subtraction, multiplication, and division
    with comprehensive error handling.
    """
    # Display available operations
    print("\nBasic Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            # Get operation choice
            choice = input("\nEnter operation number (1-5): ").strip()
            
            # Check for exit
            if choice == '5':
                print("Thank you for using the calculator!")
                break
                
            # Validate operation choice
            if choice not in ['1', '2', '3', '4']:
                print("Error: Invalid operation! Please enter a number between 1 and 5.")
                continue
                
            # Get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on choice
            if choice == '1':
                result = num1 + num2
                operator = '+'
            elif choice == '2':
                result = num1 - num2
                operator = '-'
            elif choice == '3':
                result = num1 * num2
                operator = '*'
            else:  # choice == '4'
                # Handle division by zero
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2
                operator = '/'
            
            # Display result with proper formatting
            print(f"\nResult: {num1} {operator} {num2} = {result:.2f}")
            
        except ValueError:
            print("Error: Invalid input! Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\nCalculator terminated by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    calculator()
