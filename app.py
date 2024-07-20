#importing libraries
from flask import Flask, render_template, request, jsonify
import chatbot
import json
import random

app = Flask(__name__)

# Load intents
with open('intents.json') as f:
    intents = json.load(f)

#creating a list of questions to randomly choose from
questions_list = []
for intent in intents['intents']:
    if intent["tag"] not in ("greeting", "farewell", "thanks", "provide_order_number", "product_details_follow_up", "fallback"):
        questions_list.extend(intent["patterns"])

#tracking already asked questions
asked_questions = set()

#function to get randomly shuffled suggestions
def get_random_questions():
    available_questions = [q for q in questions_list if q not in asked_questions]
    
    if not available_questions:
        # Reset asked questions if all have been used
        asked_questions.clear()
        available_questions = questions_list.copy()
        
    suggested_questions = random.sample(available_questions, min(3, len(available_questions)))
    
    # Mark the suggested questions as asked
    asked_questions.update(suggested_questions)
    
    return suggested_questions

#different routes for the app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_suggestions", methods=['GET'])
def get_suggestions():
    questions = get_random_questions()
    return jsonify(questions)

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    asked_questions.update(user_text)
    return str(chatbot.chatbot_response(user_text))


if __name__ == "__main__":
    app.run(port=8000, debug=True)
