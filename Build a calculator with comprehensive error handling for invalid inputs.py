def calculate():
    print("--- Robust Python Calculator ---")
    print("Type 'exit' at any time to quit.")

    while True:
        try:
            # 1. Get user input
            num1_raw = input("\nEnter first number: ").strip()
            if num1_raw.lower() == 'exit': break
            
            operator = input("Enter operator (+, -, *, /): ").strip()
            if operator.lower() == 'exit': break
            
            num2_raw = input("Enter second number: ").strip()
            if num2_raw.lower() == 'exit': break

            # 2. Convert to float (Handles ValueError)
            n1 = float(num1_raw)
            n2 = float(num2_raw)

            # 3. Perform Logic (Handles ZeroDivisionError and Logic Errors)
            if operator == '+':
                result = n1 + n2
            elif operator == '-':
                result = n1 - n2
            elif operator == '*':
                result = n1 * n2
            elif operator == '/':
                if n2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = n1 / n2
            else:
                raise ValueError(f"Invalid operator: '{operator}'")

        except ValueError as ve:
            print(f"Input Error: {ve}. Please enter valid numbers and operators.")
        except ZeroDivisionError as zde:
            print(f"Math Error: {zde}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        else:
            # This runs only if no exceptions were raised
            # Format the result to remove .0 if it's a whole number
            formatted_result = int(result) if result.is_integer() else result
            print(f"Result: {n1} {operator} {n2} = {formatted_result}")

    print("Calculator closed.")

if __name__ == "__main__":
    calculate()
