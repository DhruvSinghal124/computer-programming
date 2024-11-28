# Problem 14: Flatten a list of lists
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

# Test the function
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten_list(list_of_lists))

