# Problem 10: Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Test the function
print(count_vowels("Hello World"))

