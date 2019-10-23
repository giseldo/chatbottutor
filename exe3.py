# https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=5
# Chitchat
# Now you're going to leave the simple EchoBot behind and create a bot which can answer simple questions such as "What's your name?" and "What's today's weather?"
# You'll use a dictionary with these questions as keys and the correct responses as values.
# This means the bot will only respond correctly if the message matches exactly, which is a big limitation. In later exercises you will create much more robust solutions.

# Instructions 1/2
# The send_message() function has already been defined for you, as well as the bot_template and user_template variables.
# Define a respond() function which takes in a message argument, checks if the message has a pre-defined response, and returns the response in the responses dictionary if there is a match, or the "default" message otherwise.


# Define variables
name = "Greg"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

# Return the matching response if there is one, default otherwise
def ____(____):
    # Check if the message is in the responses
    if ____ in ____:
        # Return the matching message
        bot_message = ____[____]
    else:
        # Return the "default" message
        bot_message = ____["____"]
    return bot_message
