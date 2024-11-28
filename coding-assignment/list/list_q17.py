# Problem 17: Rotate a list by n positions
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

# Test the function
numbers = [1, 2, 3, 4, 5]
print(rotate_list(numbers, 2))

