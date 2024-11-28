q2
# Python code to greet a friend in a unique way

# Function to create a greeting for a friend
def create_greeting(friend_name, favorite_drink):
    return f'Hello {friend_name.capitalize()}, I hope you are having a wonderful day! Would you like a glass of {favorite_drink.capitalize()}?'

# Taking user's input
name_input = input()
drink_input = input()

# Call function and print the greeting
print(create_greeting(name_input, drink_input))
