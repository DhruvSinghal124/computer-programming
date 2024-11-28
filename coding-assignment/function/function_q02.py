# Problem 2: Check if two strings are anagrams
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Test the function
print(is_anagram("listen", "silent"))

