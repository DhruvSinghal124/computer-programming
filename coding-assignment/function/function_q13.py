# Problem 13: Check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Test the function
print(is_palindrome(121))

