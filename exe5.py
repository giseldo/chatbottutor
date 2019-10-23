https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=7

ELIZA I: asking questions

Asking questions is a great way to create an engaging conversation. Here, you'll create the very first hint of ELIZA's famous personality, by responding to statements with a question and responding to questions with answers.

A dictionary of responses with "question" and "statement" as keys and lists of appropriate responses as values has already been defined for you. Explore this in the Shell with responses.keys() and responses["question"].




    Define a respond() function which takes in message as an argument, and uses the string's .endswith() method to check if a message ends with a question mark.
    If the message does end with a question mark, choose a random "question" from the responses dictionary. Else, choose a random "statement" from the responses.
    Send the bot multiple messages with and without a question mark - these have been provided for you. If you want to experiment further in the Shell, be sure to first hit 'Run Code'.
