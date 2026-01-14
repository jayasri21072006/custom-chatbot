from app.api_client import GroqClient

class ChatManager:
    def __init__(self):
        self.client = GroqClient()
        self.history = []
    
    def get_response(self, user_message):
       self.history.append({"role": "user", "content": user_message})

    # Build messages for Groq: include conversation history
       messages = []
       for msg in self.history[-10:]:  # last 10 messages
           messages.append({"role": msg["role"], "content": msg["content"]})

       ai_response = self.client.get_response(messages)  # update api_client to accept list

       self.history.append({"role": "assistant", "content": ai_response})
       return ai_response


   