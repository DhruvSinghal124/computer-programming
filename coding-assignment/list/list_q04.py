# Problem 4: Remove all occurrences of an element
def remove_occurrences(lst, value):
    return [item for item in lst if item != value]

# Test the function
numbers = [1, 2, 3, 2, 4, 2, 5]
print(remove_occurrences(numbers, 2))

