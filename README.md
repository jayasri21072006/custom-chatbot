
# **PWGPT Chat Application**

PWGPT is an AI-powered chat application that allows users to interact with a conversational AI model. This application provides concise answers to user queries and offers detailed explanations when requested.

### **Features:**

- User-friendly chat interface
- Concise responses for general queries
- Detailed explanations for programming-related questions
- Code block support with syntax highlighting

### **Prerequisites:**

Before you begin, ensure you have the following installed:

- Anaconda or Miniconda
- Python 3.11

### **Setup Instructions:**

1. Create a Conda Environment:
   - Run the following command to create a new Conda environment named `gptenv` with Python 3.11:
     ```
     conda create -n gptenv python==3.11 -y
     ```

2. Activate the Environment:
   - Activate the newly created environment with:
     ```
     conda activate gptenv
     ```

3. Install Requirements:
   - Install the necessary dependencies using pip:
     ```
     pip install -r requirements.txt
     ```

4. Run the Application:
   - Start the application by running:
     ```
     python app.py
     ```

### **Usage:**

Once the application is running, open your web browser and navigate to `http://127.0.0.1:5000/` to access the chat interface. You can start asking questions, and the AI will respond based on your input.