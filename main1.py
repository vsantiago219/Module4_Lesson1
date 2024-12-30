import text_utils as tu  # Importing text_utils module with an alias 'tu'

# Ask the user for a string input
user_input = input("Enter a string to manipulate: ")

# Using the functions from the text_utils module with the alias 'tu'
reversed_str = tu.reverse_string(user_input)
capitalized_str = tu.capitalize_string(user_input)

# Displaying the results
print(f"Reversed string: {reversed_str}")
print(f"Capitalized string: {capitalized_str}")
