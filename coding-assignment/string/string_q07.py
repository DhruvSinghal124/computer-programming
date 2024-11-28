# Problem 7: Count occurrences of a character in a string
def count_character(string, char):
    return string.count(char)

# Example usage
string = "hello world"
char = "o"
print(f"'{char}' appears {count_character(string, char)} times in '{string}'.")

