# Problem 20: Remove element at specific index
def remove_at_index(lst, index):
    if 0 <= index < len(lst):
        return lst[:index] + lst[index + 1:]
    return lst

# Test the function
numbers = [1, 2, 3, 4, 5]
print(remove_at_index(numbers, 2))

