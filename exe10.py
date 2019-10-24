https://campus.datacamp.com/courses/building-chatbots-in-python/understanding-natural-language?ex=3

Intent classification with regex II

With your patterns dictionary created, it's now time to define a function to find the intent of a message.

Instructions
    Iterate over the intents and patterns in the patterns dictionary using its .items() method.
    Use the .search() method of pattern to look for keywords in the message.
    If there is a match, return the corresponding intent.
    Call your match_intent() function inside respond() with message as the argument and then hit 'Submit Answer' to see how the bot responds to the provided messages.

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in ____:
        # Check if the pattern occurs in the message 
        if ____:
            matched_intent = ____
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = ____
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

# Send messages
send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")
