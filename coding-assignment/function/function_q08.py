# Problem 8: Check if a number is perfect
def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Test the function
print(is_perfect(28))

