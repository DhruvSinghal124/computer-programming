# Problem 2: Find the second largest element
def second_largest(lst):
    lst.sort()
    return lst[-2]

# Test the function
numbers = [10, 20, 4, 45, 99]
print(second_largest(numbers))

