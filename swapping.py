# Function to swap two values
def swap_values(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    # Swapping values using tuple unpacking
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")
    return a, b

# Example usage
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
a, b = swap_values(a, b)
