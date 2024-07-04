# Function to print the multiplication table for a given number up to a given range
def print_multiplication_table(number, upto):
    print(f"Multiplication Table for {number}:")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

# Example usage
number = int(input("Enter the number for the multiplication table: "))
upto = int(input("Enter the range up to which you want the table: "))
print_multiplication_table(number, upto)
