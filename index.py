import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret')

# # Set up OpenAI API
# openai.api_key = os.environ.get('OPENAI_API_KEY')

link = 'https://graph.facebook.com/v16.0/118259757911348/messages'

#Test Route
@app.route('/')
def start():
    return "Works!"

# # Handle incoming messages
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     print(os.environ.get('OPENAI_API_KEY'), os.environ.get('SECRET_KEY'))
#     data = request.json
#     for message in data['messages']:
#         if message['type'] == 'chat':
#             chat_id = message['chatId']
#             message_text = message['body']
#             process_message(chat_id, message_text)
#     return jsonify({'success': True})

# # Process incoming messages
# def process_message(chat_id, message_text):
#     # TODO: Implement logic to store user data in a database

#     # Get response from OpenAI API
#     response = get_response(message_text)

#     # Send response to user
#     send_message(chat_id, response)

# # Get response from OpenAI API
# def get_response(prompt):
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     message = response.choices[0].text.strip()
#     return message

# # Send message to user
# def send_message(chat_id, message):
#     # TODO: Implement logic to send message to user via WhatsApp Business API
#     pass

if __name__ == '__main__':
    app.run(debug=True)
