# Problem 6: Find the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function
print(gcd(60, 48))

