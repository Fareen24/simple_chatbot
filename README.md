## Overview

This project implements a simple chatbot using natural language processing techniques to engage in conversations. The chatbot reads dialogue pairs from a text file and responds to user queries based on the most relevant dialogue.

## Features

- **Natural Language Processing:** Utilizes tokenization, lemmatization, and custom stopwords for processing user input.
- **Contextual Responses:** Finds the most relevant dialogue response based on user queries.
- **Streamlit Application:** A user-friendly web interface for interaction.


## Instructions

1. Choose a topic: Choose a topic that you are interested in and find a text file related to that topic. You can use websites such as Project Gutenberg to find free text files.

2. Preprocess the data: Modify the preprocess() function in the code provided to preprocess the data in your text file. You may want to modify the stop words list or add additional preprocessing steps to better suit your needs.

3. Define the similarity function: Modify the get_most_relevant_sentence() function to compute the similarity between the user's query and each sentence in your text file. You may want to modify the similarity metric or add additional features to improve the performance of your chatbot.

4. Define the chatbot function: Modify the chatbot() function to return an appropriate response based on the most relevant sentence in your text file.

5. Create a Streamlit app: Use the main() function in the code provided as a template to create a web-based chatbot interface. Prompt the user for a question, call the chatbot() function to get the response, and display it on the screen.
Note:
