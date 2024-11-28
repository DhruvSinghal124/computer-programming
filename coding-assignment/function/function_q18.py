# Problem 18: Sum of digits of a number
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

# Test the function
print(sum_of_digits(12345))

