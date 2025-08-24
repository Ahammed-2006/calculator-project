from app.add import add
from app.subtract import subtract
from app.multiply import multiply
from app.divide import divide

if __name__ == "__main__":
    a, b = 10, 5
    print(f"Add: {a} + {b} = {add(a, b)}")
    print(f"Subtract: {a} - {b} = {subtract(a, b)}")
    print(f"Multiply: {a} * {b} = {multiply(a, b)}")
    print(f"Divide: {a} / {b} = {divide(a, b)}")
