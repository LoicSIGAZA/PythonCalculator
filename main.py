import calculator

def main():
    print("Simple Python Calculator")
    print("Operations: add, subtract, multiply, divide")

    while True:
        op = input("Enter operation (or 'exit' to quit): ").strip().lower()
        if op == 'exit':
            break
        if op not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Try again.")
            continue

        try:
            if op == 'add':
                result = calculator.add(a, b)
            elif op == 'subtract':
                result = calculator.subtract(a, b)
            elif op == 'multiply':
                result = calculator.multiply(a, b)
            elif op == 'divide':
                result = calculator.divide(a, b)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
