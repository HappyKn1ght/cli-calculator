import math

def menu():
    print("""========= CALCULATOR =========
--- Basic Operations ---
  1. Addition (+)          5. Floor Div (//)
  2. Subtraction (-)       6. Modulus (%)
  3. Multiplication (*)    7. Power (**)
  4. Division (/)

--- Scientific Operations ---
  8. Square Root (sqrt)   11. Sine (sin)
  9. Factorial (fact)     12. Cosine (cos)
 10. Logarithm (log)      13. Tangent (tan)

--- Controls ---
  =  Show Final Result     c  Clear / Reset
  q  Quit Calculator
=========================================
""")


def basic_operations(result, op):
    num2 = input("Enter number: ")

    try:
        num2 = float(num2)
        if not math.isfinite(num2):
            print("Invalid number!")
        else:
            match op:
                case "1" | "+":
                    result += num2

                case "2" | "-":
                    result -= num2

                case "3" | "*":
                    result *= num2

                case "4" | "/":
                    if num2 == 0:
                        print("Cannot divide by zero!")
                    else:
                        result /= num2

                case "5" | "//":
                    if num2 == 0:
                        print("Cannot divide by zero!")
                    else:
                        result //= num2

                case "6" | "%":
                    if num2 == 0:
                        print("Cannot divide by zero!")
                    else:
                        result %= num2

                case "7" | "**":
                    result **= num2

    except ValueError:
        print("Invalid Input!\nEnter Numbers only")
    return result


def scientific_operations(result, op):
    match op:
        case "8" | "sqrt":
            if result < 0:
                print("Cannot calculate square root of a negative number!")
            else:
                result = math.sqrt(result)

        case "9" | "fact":
            if result < 0 or not result.is_integer():
                print("Factorial requires a non-negative whole number!")
            else:
                result = float(math.factorial(int(result)))

        case "10" | "log":
            if result <= 0:
                print("Logarithm requires a positive number!")
            else:
                result = math.log10(result)

        case "11" | "sin":
            result = math.sin(math.radians(result))

        case "12" | "cos":
            result = math.cos(math.radians(result))

        case "13" | "tan":
            result = math.tan(math.radians(result))
    return result

def main():
    menu()
    while True:
        try:
            result = float(input("Enter Number: "))
            if not math.isfinite(result):
                print("Invalid number!")
                continue

        except ValueError:
            print("Invalid Input!\nEnter Number only!")
            continue


        while True:
            print(f"\nCurrent Result: {result}")
            op = input("Choose operation (1-13) or (=, c, q): ").lower().strip()

            if op == 'q':
                print("Exiting Calculator. Goodbye!")
                return

            elif op == '=':
                print(f"Final Result: {result}")
                break

            elif op == 'c':
                print("Calculator Cleared!")
                break

            elif op in ("1", "+", "2", "-", "3", "*", "4", "/", "5", "//", "6", "%", "7", "**"):
                result = basic_operations(result, op)

            elif op in ("8", "sqrt", "9", "fact", "10", "log", "11", "sin", "12", "cos", "13", "tan"):
                result = scientific_operations(result, op)

            else:
                print("Invalid option! Please choose from the menu.")



if __name__ == "__main__":
    main()
