# Problem 8: Find common elements in tuples
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
intersection = tuple(set(t1) & set(t2))
print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Common Elements:", intersection)

