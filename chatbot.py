import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary NLTK data (only once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Sample corpus
corpus = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Ask me anything.",
    "how are you": "I'm just a bot, but I'm functioning well!",
    "bye": "Goodbye! Have a nice day.",
    "what is your name": "I'm a simple NLP chatbot.",
    "what can you do": "I can answer your basic queries using simple NLP.",
}

# Preprocessing
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stopwords.words('english') and word not in string.punctuation]
    return tokens

# Main response generator
def generate_response(user_input):
    user_input = user_input.lower()
    for question, answer in corpus.items():
        if user_input in question:
            return answer
    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Chat loop
print("🤖 Chatbot is ready! Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! 👋")
        break
    response = generate_response(user_input)
    print("Chatbot:", response)



