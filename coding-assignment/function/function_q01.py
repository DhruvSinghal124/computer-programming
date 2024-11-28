# Problem 1: Sum of all numbers in a list
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Test the function
numbers = [1, 2, 3, 4, 5]
print("Sum of the list:", sum_of_list(numbers))

