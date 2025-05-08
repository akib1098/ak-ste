try:
    n = int(input("Enter the number of inputs: "))
    if n <= 0:
        raise ValueError("Number of inputs must be greater than zero.")
    result = 0
    for i in range(n):
        try:
            a = int(input(f"Enter number {i+1}: "))
            result += a
        except ValueError:
            print("Invalid input. Please enter an integer.")
            exit()
    print(f"The average is: {result/n}")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a valid number of inputs.")
except ValueError as e:
    print(e)
    