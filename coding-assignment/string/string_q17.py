# Problem 17: Reverse the order of words in a string
def reverse_words(string):
    return ' '.join(string.split()[::-1])

# Example usage
string = "Python is amazing"
print(f"Reversed words: '{reverse_words(string)}'.")

