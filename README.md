# AI-Based Support Chatbot for E-Commerce Website

## Overview
This project involves creating an AI-based support chatbot for an e-commerce website. The chatbot is designed to assist users by answering their queries and providing suggestions for common questions.

### Key Features
The chatbot is capable of answering a variety of common customer queries, for example:

- **Return policy**
- **Shipping options**
- **Payment methods**
- **Order status**
- **Discounts and promotions**

## Technologies Used

- **Programming Languages & Frameworks:** Python, JavaScript, HTML, CSS, Flask
- **Data Processing & AI:** NLTK, TensorFlow, Keras

## Approach

### Step 1: Data Preprocessing
Data preprocessing is the foundation of the AI model. The process involves loading data from `intents.json`, preprocessing it using NLTK to tokenize and lemmatize the text, and preparing it for the AI model. This step ensures that the data is clean and structured for effective model training.

- **Code Implementation:** `training.py`
- **Key Tasks:** Data loading, tokenization, lemmatization, vectorization

### Step 2: Model Creation and Training
The AI model is created and trained using TensorFlow and Keras. The preprocessed data is fed into the model, which is then trained to understand and classify user intents accurately.

- **Code Implementation:** `training.py`
- **Key Tasks:** Model creation, model training, saving the trained model

### Step 3: User Input Processing and Response Prediction
Using the trained model, the chatbot processes user inputs, predicts the relevant intents, and generates appropriate responses. This functionality is encapsulated in reusable functions, making it easy to integrate with the web application.

- **Code Implementation:** `chatbot.py`
- **Key Tasks:** Model loading, input preprocessing, intent prediction, response generation

### Step 4: Web Application Development
A web application is developed to provide a user interface for the chatbot. Users can input their questions, and the chatbot responds through the backend using the functions created in the previous step. The frontend is designed using HTML, CSS, and JavaScript, while Flask handles the backend logic.

- **Code Implementation:** `app.py` (Flask), `index.html`, `scripts.js`, `styles.css`

## Unique Features

- **Question Suggestion Feature:** Displays relevant questions to users, enhancing the user experience. The backend processes these suggestions similarly to direct user input and ensures previously suggested questions are not repeated.
- **Toggle Chatbot Visibility:** A closing button hides the chatbot on the frontend, and an icon is provided to make it reappear when clicked.

## Files Explained

- **intents.json:** Contains the training data, including various user intents, examples, and responses.
- **training.py:** Handles data preprocessing, model creation, and training.
- **chatbot.py:** Contains functions for preprocessing user inputs, predicting intents, and generating responses.
- **app.py:** Flask application to manage the backend logic and API endpoints.
- **index.html:** The main HTML file for the web application frontend.
- **scripts.js:** JavaScript file to handle frontend interactivity and AJAX requests.
- **styles.css:** CSS file for styling the web application.

## Challenges Faced

- **Distinguishing Between Similar Intents:** Initially, the model struggled to differentiate between greeting and farewell tags. This was resolved by refining the intents in the `intents.json` file.
- **Fallback Responses:** The model often misclassified random or out-of-context inputs as greetings. Various attempts to adjust hyperparameters and intent content failed. The solution was to change the model optimizer from SGD to Adam, which significantly improved the model's performance in handling fallback scenarios.
