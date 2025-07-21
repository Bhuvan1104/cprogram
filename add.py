# add.py
import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add.py <num1> <num2>")
        sys.exit(1)

    a = float(sys.argv[1])
    b = float(sys.argv[2])

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {sub(a, b)}")
    print(f"Multiplication: {mul(a, b)}")
    print(f"Division: {div(a, b)}")
