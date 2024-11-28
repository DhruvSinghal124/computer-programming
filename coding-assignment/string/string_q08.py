# Problem 08: Find the longest word in a string
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example usage
sentence = "Python programming is amazing"
print(f"The longest word in the sentence is '{longest_word(sentence)}'.")

