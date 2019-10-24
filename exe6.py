https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=9

ELIZA II: Extracting key phrases

The really clever thing about ELIZA is the way the program appears to understand what you told it by occasionally including phrases uttered by the user in its responses.

In this exercise, you will match messages against some common patterns and extract phrases using re.search(). A dictionary called rules has already been defined, which matches the following patterns:

    "do you think (.*)"
    "do you remember (.*)"
    "I want (.*)"
    "if (.*)"

Inspect this dictionary in the Shell before starting the exercise.

Instructions

    Iterate over the rules dictionary using its .items() method, with pattern and responses as your iterator variables.
    Use re.search() with the pattern and message to create a match object.
    If there is a match, use random.choice() to pick a response.
    If '{0}' is in that response, use the match object's .group() method with index 1 to retrieve a phrase.
