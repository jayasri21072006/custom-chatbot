from flask import Blueprint, render_template, request, jsonify, current_app
from app.utils import format_response

# 1. Initialize the Blueprint
# 'main' matches the name used in your app.register_blueprint() call
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Renders the main study portal. 
    Make sure your HTML file is named 'chat.html' in the /templates folder.
    """
    return render_template('chat.html')

@main.route('/api/chat', methods=['POST'])
def chat():
    """
    Main API endpoint for the chatbot.
    Receives JSON: {"message": "User query here"}
    """
    # Extract the message from the POST request
    data = request.get_json()
    user_message = data.get('message')
    
    # Basic validation
    if not user_message:
        return jsonify({"error": "Kelvi ketunga! (Please ask a question!)"}), 400
    
    try:
        # 2. Call the tuned Guru Bot
        # We access the bot using current_app because it was attached in __init__.py
        ai_response = current_app.guru_bot.get_response(user_message)

        # 3. Format the response
        # This converts the raw AI text into clean HTML/Markdown for your chat window
        formatted_response = format_response(ai_response)

        return jsonify({
            "status": "success",
            "response": formatted_response
        })
        
    except Exception as e:
        # Log the error for debugging
        print(f"Chat Error: {str(e)}")
        return jsonify({
            "status": "error",
            "response": "(Something went wrong!) Please try again later."
        }), 500