Problem 3: Remove Duplicates from a String
Description: Write a program to remove duplicate characters from a string.

def remove_duplicates(input_string):
    return "".join(sorted(set(input_string), key=input_string.index))

# Example usage
print(remove_duplicates("banana"))
