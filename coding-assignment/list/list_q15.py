# Problem 15: Most frequent element
from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

# Test the function
numbers = [1, 2, 3, 3, 3, 4, 5]
print(most_frequent(numbers))

