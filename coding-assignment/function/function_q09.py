# Problem 9: Longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Test the function
print(longest_word("I love programming in Python"))

