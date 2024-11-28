# Problem 5: Factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test the function
print(factorial(5))

