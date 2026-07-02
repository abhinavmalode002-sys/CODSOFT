def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2


def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose an operation (or 'q' to quit): ")

        if choice.lower() == 'q':
            break
        elif choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please choose a valid operation.")
            continue

        try:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")

            else:
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            cont_choice = input("\nPerform another calculation? (Y/N): ").upper()

            if cont_choice != "Y":
                break

        except ZeroDivisionError as e:
            print(e)


if __name__ == "__main__":
    main()