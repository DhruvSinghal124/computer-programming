Problem 6: Find First and Last Characters of a String
Description: Write a program that returns the first and last characters of the given string.

def first_and_last_char(input_string):
    if len(input_string) < 2:
        return ""
    return input_string[0] + input_string[-1]

# Example usage
print(first_and_last_char("hello"))
