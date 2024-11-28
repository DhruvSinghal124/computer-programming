# Problem 15: Prime numbers in a range
def primes_in_range(start, end):
    primes = []
    for num in range(start, end+1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

# Test the function
print(primes_in_range(10, 20))

