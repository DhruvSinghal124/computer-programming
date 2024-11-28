# Problem 6: Intersection of two lists
def intersection(list1, list2):
    return [item for item in list1 if item in list2]

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(intersection(list1, list2))

