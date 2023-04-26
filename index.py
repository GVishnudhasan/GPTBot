# import openai
# import pymongo
# import os
# import requests
# import json
# from flask import Flask, request, jsonify
# from dotenv import load_dotenv

# load_dotenv()

# # Setup MongoDB connection
# client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
# db = client["whatsappbot"]

# # Setup OpenAI API
# openai.api_key = os.environ.get("OPENAI_API_KEY")

# # Setup Flask server
# app = Flask(__name__)

# # Setup WhatsApp Business API
# BASE_URL = "https://api.chat-api.com/instance{}/{}"

# def send_message(chat_id, message):
#     url = BASE_URL.format(os.environ.get("CHAT_API_INSTANCE_ID"), "sendMessage")
#     data = {"chatId": chat_id, "body": message}
#     headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.environ.get('CHAT_API_TOKEN')}"}
#     response = requests.post(url, data=json.dumps(data), headers=headers)
#     return response.json()

# def process_message(chat_id, message):
#     # Check if it is the user's first time chatting
#     user = db.users.find_one({"chat_id": chat_id})
#     if not user:
#         # Welcome message
#         send_message(chat_id, "Welcome to our WhatsApp bot! Please enter your name:")
#         db.users.insert_one({"chat_id": chat_id, "state": "name"})
#     else:
#         # Handle message based on user's state
#         state = user["state"]
#         if state == "name":
#             # Store user's name in database and ask for profession
#             db.users.update_one({"chat_id": chat_id}, {"$set": {"name": message, "state": "profession"}})
#             send_message(chat_id, "Thanks! What is your profession?")
#         elif state == "profession":
#             # Store user's profession in database and ask for college
#             db.users.update_one({"chat_id": chat_id}, {"$set": {"profession": message, "state": "college"}})
#             send_message(chat_id, "Great! Where did you study?")
#         elif state == "college":
#             # Store user's college in database and ask a hardcoded question
#             db.users.update_one({"chat_id": chat_id}, {"$set": {"college": message, "state": "hardcoded_question"}})
#             send_message(chat_id, "Nice! Do you prefer Apple or Android phones?")

#             # Add options as buttons using WhatsApp message templates
#             options = [{"title": "Apple", "type": "reply", "payload": "apple"}, 
#                        {"title": "Android", "type": "reply", "payload": "android"}]
#             data = {"chatId": chat_id, 
#                     "template": {"type": "button", "text": "Please select an option:", "buttons": options}}
#             url = BASE_URL.format(os.environ.get("CHAT_API_INSTANCE_ID"), "sendTemplate")
#             headers = {"Content-Type": "application/json", "Authorization": f"Bearer {os.environ.get('CHAT_API_TOKEN')}"}
#             response = requests.post(url, data=json.dumps(data), headers=headers)
#         elif state == "hardcoded_question":
#             # Use OpenAI to answer user's question
#             response = openai.Completion.create(engine="davinci", prompt=message, max_tokens=1024)
#             answer = response.choices[0].text.strip()
#             send_message(chat_id, answer)

# # Handle incoming messages
# @app.route("/webhook", methods=["POST"])
# def webhook():
#     data = request.json
#     for message in data["messages"]:
#         if message["type"] == "chat":
#             chat_id = message["chatId"]
#             message_text = message["body"]
#             process_message(chat_id, message_text)
#     return jsonify({"success": True})

# if __name__ == "__main__":
#     app.run(debug=True)

import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret')

# Set up OpenAI API
openai.api_key = os.environ.get('OPENAI_API_KEY')

link = 'https://graph.facebook.com/v16.0/118259757911348/messages'

#Test Route
@app.route('/')
def start():
    return "Works!"

# Handle incoming messages
@app.route('/webhook', methods=['POST'])
def webhook():
    print(os.environ.get('OPENAI_API_KEY'), os.environ.get('SECRET_KEY'))
    data = request.json
    for message in data['messages']:
        if message['type'] == 'chat':
            chat_id = message['chatId']
            message_text = message['body']
            process_message(chat_id, message_text)
    return jsonify({'success': True})

# Process incoming messages
def process_message(chat_id, message_text):
    # TODO: Implement logic to store user data in a database

    # Get response from OpenAI API
    response = get_response(message_text)

    # Send response to user
    send_message(chat_id, response)

# Get response from OpenAI API
def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# Send message to user
def send_message(chat_id, message):
    # TODO: Implement logic to send message to user via WhatsApp Business API
    pass

if __name__ == '__main__':
    app.run(debug=True)
