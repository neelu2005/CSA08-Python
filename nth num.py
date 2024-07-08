def find_nth_largest(numbers, N):
    if N > len(numbers) or N <= 0:
        return None
    
    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    
    # Return the Nth largest number
    return sorted_numbers[N-1]

# Sample Input
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
N = 3

# Finding the Nth largest number
nth_largest = find_nth_largest(numbers, N)

# Output the result
if nth_largest is not None:
    print(f"The {N}th largest number is: {nth_largest}")
else:
    print(f"Invalid value for N: {N}")
