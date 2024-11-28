# Problem 2: Merge two dictionaries with summed values for overlapping keys
dict1 = {'Alice': 25, 'Bob': 30}
dict2 = {'Bob': 20, 'Charlie': 35}
merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
print("Merged Dictionary:", merged_dict)

