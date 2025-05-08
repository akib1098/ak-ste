def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = add(input1, input2)
elif operation == '-':
    result = subtract(input1, input2)
elif operation == '*':
    result = multiply(input1, input2)
elif operation == '/':
    try:
        result = divide(input1, input2)
    except ValueError as e:
        print(e)
        result = None
else:
    raise ValueError("Invalid operation")
print(f"The result is: {result}")