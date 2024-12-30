def mood_response(mood):
    # Implementing response logic based on the mood
    mood = mood.lower()  # Make the input lowercase to handle case insensitivity
    
    if mood == "happy":
        return "That's great! Hope that feeling continues to grow!"
    elif mood == "sad":
        return "I'm sorry to hear that. I hope your day gets better soon."
    elif mood == "excited":
        return "Awesome! Remember the reason you feel this way and keep it going!"
    elif mood == "angry":
        return "Breathe. Not all days or times will be happy. Try to stay calm and focus on something positive."
    elif mood == "anxious":
        return "I know things can be overwheliming. Take in some deep breaths."
    else:
        return "Take care of yourself today."


