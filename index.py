import os
import openai
import requests
from flask import Flask, request, jsonify

# Set up OpenAI credentials
openai.api_key = "YOUR_OPENAI_API_KEY"

# Set up Flask server
app = Flask(__name__)

# Define endpoint for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get message details from WhatsApp Business API webhook
    data = request.get_json()
    sender = data['messages'][0]['from']
    message = data['messages'][0]['text']

    # Store user data in database (you'll need to set up your own database for this)
    # ...

    # Use OpenAI to generate response
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send response back to user using WhatsApp Business API
    url = "https://graph.facebook.com/v16.0/118259757911348/messages"
    headers = {
        "Authorization": "Bearer EABTHNf0nHU8BAAiGqqCtbiJACanfQoRQZC03drtaTZA9fuECKAsbDdwcW6ZC0NCsHrTF5Cxk56bd24BlX2JoYLZC3vpmZAwxr226qDD28EwDcaIFFYHvjpA45AO2UWEByxPHl8ZCs330kZCrypkeo6ott8Vhk9ZABkDp101a02XqlWJAiQvyHXWdCFhqfWkyARZCC9qZAohw9uwgZDZD",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": sender,
        "type": "text",
        "text": response.choices[0].text,
    }
    response = requests.post(url, headers=headers, json=payload)

    return jsonify({'success': True})

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
