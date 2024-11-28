# Problem 4: Find common elements between two lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
print("Common elements:", common_elements(list1, list2))

