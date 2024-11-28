# Problem 12: Remove all occurrences of an element from a list
def remove_element(lst, element):
    return [x for x in lst if x != element]

# Test the function
print(remove_element([1, 2, 3, 4, 2, 5], 2))

