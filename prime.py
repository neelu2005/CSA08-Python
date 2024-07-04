def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_non_primes(start, end):
    non_primes = []
    for num in range(start, end + 1):
        if not is_prime(num):
            non_primes.append(num)
    return non_primes

# Define the range
start = 5
end = 12

# Find non-prime numbers in the range
non_prime_numbers = find_non_primes(start, end)

# Print the result
print(f"Non-prime numbers between {start} and {end} are: {non_prime_numbers}")
