# Problem 14: Check if a string is a valid email
def is_valid_email(string):
    return "@" in string and "." in string

# Example usage
string = "example@gmail.com"
print(f"'{string}' is a valid email: {is_valid_email(string)}.")

