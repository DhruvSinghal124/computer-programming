# Problem 11: LCM of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Test the function
print(lcm(4, 5))

