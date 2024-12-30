import mood_responses

# Asking the user how they are feeling
mood = input("How are you feeling today? ")

# Calling the mood_response function from the mood_responses module
response = mood_responses.mood_response(mood)

# Printing the response
print(response)