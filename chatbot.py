#importing librarbies
import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')
from tensorflow.keras.models import load_model # type: ignore

lemmatizer = WordNetLemmatizer()

#loading the model
model = load_model("models/chatbot_model.h5")

#loading the intents data
intents = json.loads(open('intents.json').read())

#loading words and classes
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
ignore_letters = ["?","!",",",".","'"]


#function to tokenize and lemmatize the sentence from user
def clean_up_sentence(sentence):
    sentence_words =  nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words if word not in ignore_letters]

    return sentence_words


#function to make sentence suitbale for model prediction using bag of words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i]=1

    return (np.array(bag),sentence_words)


#predicting the classes and their corresponding confidence scores for the given sentence, also applyting a threshold value
def predict_class(sentence):
    bow,sentence_words = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.5
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x:x[1], reverse = True)
    return_list = []
    for r in results:
        return_list.append({'intent':classes[r[0]],'probability':str(r[1])})
    
    return (return_list,sentence_words)


#based on the class of the sentence, finding a suitable response from the intents data of same tag
def get_response(intents_list,intents_json):
    tag = intents_list[0]['intent']

    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break

    return result


#function used to provide response for the user input by utilizing the other functions
def chatbot_response(message):
    ints, sentence_words = predict_class(message)
    if len(ints) == 0:
        return random.choice([resp for intent in intents['intents'] if intent['tag'] == 'fallback' for resp in intent['responses']])
    
    return get_response(ints, intents)


#If you want to run this code separately, uncomment the below lines and run this file

#while True:
#   mes = input("")
#   print(chatbot_response(mes))
