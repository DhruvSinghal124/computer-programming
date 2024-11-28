Problem 2: Count Vowels in a String
Description: Write a program to count the number of vowels in a given string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_string if char in vowels)

# Example usage
print(count_vowels("hello world"))
