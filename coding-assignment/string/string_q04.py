Problem 4: Check if a String is a Palindrome
Description: Write a program to check if the given string is a palindrome.

def is_palindrome(input_string):
    return input_string == input_string[::-1]

# Example usage
print(is_palindrome("radar")) 
print(is_palindrome("hello"))
