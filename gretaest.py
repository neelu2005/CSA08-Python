def find_greatest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example usage:
num1 = 5
num2 = 8
num3 = 3
greatest = find_greatest(num1, num2, num3)
print(f"The greatest number is: {greatest}")
