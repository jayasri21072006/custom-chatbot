 🤖 Custom LLM Chatbot – Flask + Groq + Tavily
 As a part of my  Gen AI learning journey I developed above repository 

A lightweight, production-ready chatbot built with **Flask**, powered by **Groq LLM API** for fast responses and **Tavily Search API** for real-time web-augmented answers.

This project is designed with clean architecture, environment-safe secrets handling, and modular components for easy extension.

 ✨ Features

* ⚡ Ultra-fast LLM inference using **Groq**
* 🌐 Real-time web search integration using **Tavily**
* 🔐 Secure API key management using `.env`
* 🧱 Modular Flask architecture
* 📁 YAML based configuration system
* 💬 Clean UI with HTML + CSS
* 🛠️ Ready for deployment

 📂 Project Structure

```
custom-chatbot/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── app/
│   ├── api_client.py
│   ├── chat.py
│   ├── routes.py
│   ├── utils.py
│   ├── templates/
│   │   └── chat.html
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── images/
│           └── custom_llm.jpg
│
├── config/
│   └── config.yaml
│
└── logger/
    └── __init__.py
⚙️ Setup Instructions

 1️⃣ Clone the Repository

```bash
git clone https://github.com/jayasri21072006/custom-chatbot.git
cd custom-chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
 4️⃣ Create `.env` file

Create a `.env` file in the root folder.

```
API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
# 5️⃣ Run the Application

```bash
python app.py
```

Now open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🔐 Security

* API keys are stored securely in `.env`
* `.env` is ignored using `.gitignore`
* No sensitive credentials are pushed to GitHub

---

## 🚀 Future Improvements

* Authentication system
* Chat history storage
* Deployment on cloud
* Voice input support
* Multiple model selection

---

## 📜 License

This project is licensed for educational and development purposes.

Jayasri T
2026 All rights reserved
---

## 🙌 Acknowledgements

* Groq LLM API
* Tavily Search API
* Flask Framework

---
JUST THE LOCAL HOST IMPLEMENTATION::


<img width="1920" height="995" alt="Screenshot (378)" src="https://github.com/user-attachments/assets/2da3720d-474b-4207-9815-ceb2c40eea8c" />


## 👨‍💻 Author

**Jayasri T**
AI / ML Developer | Data Science Enthusiast
