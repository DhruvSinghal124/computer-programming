# Problem 20: Replace multiple spaces with a single space
def normalize_spaces(string):
    return ' '.join(string.split())

# Example usage
string = "hello   world"
print(f"Normalized string: '{normalize_spaces(string)}'.")

