#importing libraries
import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')
from tensorflow.keras.optimizers import Adam # type: ignore


lemmatizer = WordNetLemmatizer()

#loading intents
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ["?","!",",",".","'"]

#tokenizing the patterns, creating classes with help of tags, and creating documents containing words and their respective class
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent["tag"])


#lemmatizing the words and removing duplicates
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))


#saving words and classes to reuse them while using the model
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

training = []
output_empty = [0]*len(classes)


#using bag of words to make the data suitable for the AI model(in 1s and 0s)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        if word in word_patterns:
            bag.append(1)
        else:
            bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append(bag+ output_row)


#shuffling and splitting training data for input and ouput
random.shuffle(training)
training = np.array(training)
train_x = training[:,:len(words)]
train_y = training[:,len(words):]


#creating the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64,activation="relu"))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(train_y[0]),activation="softmax"))


#setting hyperparameters and optimization technique
model.compile(loss='categorical_crossentropy', 
              optimizer=Adam(learning_rate=0.01), 
              metrics=['accuracy'])
              
#training the model and saving it
model.fit(train_x,train_y,epochs=300,batch_size=5,verbose=1)
model.save("chatbot_model_new.h5")

print("Done")
