# Problem 9: Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# Test the function
numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))

