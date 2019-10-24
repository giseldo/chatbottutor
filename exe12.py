https://campus.datacamp.com/courses/building-chatbots-in-python/understanding-natural-language?ex=6

word vectors with spaCy

In this exercise you'll get your first experience with word vectors! You're going to use the ATIS dataset, which contains thousands of sentences from real people interacting with a flight booking system.

The user utterances are available in the list sentences, and the corresponding intents in labels.

Your job is to create a 2D array X with as many rows as there are sentences in the dataset, where each row is a vector describing that sentence.

Instructions

    Load the spaCy English model by calling spacy.load() with argument 'en'.
    Calculate the length of sentences using len() and the dimensionality of the word vectors using nlp.vocab.vectors_length.
    For each sentence, call the nlp object with the sentence as the sole argument. Store the result as doc.
    Use the .vector attribute of doc to get the vector representation of each sentence, and store this vector in the appropriate row of X.


# Load the spacy model: nlp
nlp = ____

# Calculate the length of sentences
n_sentences = ____

# Calculate the dimensionality of nlp
embedding_dim = ____

# Initialize the array with zeros: X
X = np.zeros((n_sentences, embedding_dim))

# Iterate over the sentences
for idx, sentence in enumerate(sentences):
    # Pass each each sentence to the nlp object to create a document
    doc = ____
    # Save the document's .vector attribute to the corresponding row in X
    X[idx, :] = ____
