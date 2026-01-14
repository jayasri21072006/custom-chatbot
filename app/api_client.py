import os
from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.tavily_key = os.getenv("TAVILY_API_KEY")

        if not self.api_key or not self.tavily_key:
            raise ValueError("CRITICAL: API_KEY or TAVILY_API_KEY missing!")

        self.client = Groq(api_key=self.api_key)
        self.tavily = TavilyClient(api_key=self.tavily_key)

    def needs_web(self, text):
        keywords = ["latest", "today", "current", "news", "2026", "notification"]
        return any(k in text.lower() for k in keywords)

    def get_web_context(self, query):
        try:
            results = self.tavily.search(query=query, search_depth="advanced", max_results=2)
            return "\n".join(r["content"] for r in results.get("results", []))
        except:
            return ""

    def get_response(self, user_text):
        use_web = self.needs_web(user_text)
        live_data = self.get_web_context(user_text) if use_web else ""

        system_prompt = f"""
DATE: {datetime.now().strftime('%B %d, %Y')}
ROLE: Smart AI Assistant keep context in mind.
Be short, direct and helpful.
{live_data}
"""

        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ⚡ FAST MODEL
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            temperature=0.2,
            max_tokens=500
        )

        return completion.choices[0].message.content
