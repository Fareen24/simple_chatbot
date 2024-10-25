import nltk

# Download NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, sent_tokenize

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer

import string

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

import streamlit as st

# Load the text file and preprocess the data

def load_dialogs(file_path="dialogs.txt"):
    dialogs = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "\t" in line:
                prompt, response = line.strip().split("\t")
                dialogs.append((prompt, response))
    return dialogs

dialogs = load_dialogs()

# Define stopwords and initialize lemmatizer
custom_stopwords = set(stopwords.words('english')).union(
    {"i'm", "how", "what", "about", "yourself", "thanks", "asking", "been", 
     "going", "do", "you", "very", "much", "with", "good", "well", "there"}
)
lemmatizer = WordNetLemmatizer()

# Preprocess text
def preprocess(text):
    words = word_tokenize(text)
    words = [
        lemmatizer.lemmatize(word.lower()) for word in words 
        if word.lower() not in custom_stopwords and word not in string.punctuation
    ]
    return words

# Prepare corpus with preprocessed dialog prompts
corpus = [(preprocess(dialog[0]), dialog[1]) for dialog in dialogs]

# Function to get the most relevant response
# Function to get the most relevant response
def get_most_relevant_response(query):
    query_words = set(preprocess(query))
    max_similarity = 0
    best_response = "I'm not sure how to respond to that."

    for prompt_words, response in corpus:
        union_len = len(query_words.union(prompt_words))
        # Check if union is not empty to avoid division by zero
        if union_len > 0:
            similarity = len(query_words.intersection(prompt_words)) / float(union_len)
            if similarity > max_similarity:
                max_similarity = similarity
                best_response = response

    return best_response


# Chatbot function
def chatbot(question):
    return get_most_relevant_response(question)

# Streamlit app
def main():
    st.title("Chatbot")
    st.write("Let's talk...")

    # User question
    question = st.text_input("You:", placeholder="Type your question here...")

    # Response button
    if st.button("Submit"):
        if question.strip():
            response = chatbot(question)
            st.write("Chatbot:", response)
        else:
            st.write("Please enter a question before submitting.")

if __name__ == "__main__":
    main()
