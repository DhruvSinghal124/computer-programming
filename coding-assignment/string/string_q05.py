Problem 5: Count Character Frequency
Description: Write a program to count the frequency of each character in a string.

def count_character_frequency(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Example usage
print(count_character_frequency("google.com"))  
