# def loop(n):
#     tvalue=0
#     for i in range(n):
#         value= int(input("Enter a number{i}: "))
#         if value <= 0:
#             raise ValueError("enter again")
#         else:   
#          tvalue+= value
#     return tvalue/n


# n = int(input("Enter a number: "))
# if n <= 0:
#     raise ValueError("Negative numbers are not allowed")
# else:
#     print(loop(n))




def get_average(n):
    if n <= 0:
        raise ValueError("Number of inputs must be greater than 0")

    total = 0
    count = 0

    while count < n:
        try:
            num = int(input(f"Enter integer {count + 1}: "))
            if num <= 0:
                raise ValueError("Input must be greater than 0")
            total += num
            count += 1
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    return total / n

while True:
    try:
        n = int(input("Enter the number of integers: "))
        average = get_average(n)
        print(f"The average is: {average}")
        break
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid positive integer.")
