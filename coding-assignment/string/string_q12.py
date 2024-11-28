# Problem 12: Find the most frequent character in a string
def most_frequent_char(string):
    return max(set(string), key=string.count)

# Example usage
string = "hello world"
print(f"The most frequent character in '{string}' is '{most_frequent_char(string)}'.")

