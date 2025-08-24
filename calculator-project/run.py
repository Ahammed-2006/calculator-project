from app.add import add
from app.subtract import subtract
from app.multiply import multiply
from app.divide import divide

def main():
    print("Simple Calculator")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("Select operation: add, subtract, multiply, divide")
    operation = input("Operation: ").strip().lower()
    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            print("Invalid operation selected.")
            return
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
