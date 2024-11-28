# Problem 16: Remove duplicate words in a string
def remove_duplicate_words(string):
    words = string.split()
    return ' '.join(dict.fromkeys(words))

# Example usage
string = "hello world hello"
print(f"String after removing duplicate words: '{remove_duplicate_words(string)}'.")

