# Problem 12: Product of all elements in a list
def product_of_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product

# Test the function
numbers = [1, 2, 3, 4]
print(product_of_elements(numbers))

