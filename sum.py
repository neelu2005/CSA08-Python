def sum_of_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Read input values
N = int(input("Enter N value: "))
number = input(f"Enter {N} digit number: ")

# Check if the input is a valid N digit number
if len(number) != N or not number.isdigit():
    print("Invalid input! Please enter a valid N digit number.")
else:
    number = int(number)
    result = sum_of_digits(number)
    print(f"Sum of {N} digit number: {result}")
