from flask import Flask, render_template, request, jsonify 
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize Flask app
app = Flask(__name__)

# Define the template for conversation
template = """
Answer the question below.

Here is the conversation history:{context}

Question:{question}

Answer:
"""

# Initialize the model and prompt
model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Define conversation context
context = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    global context
    user_input = request.form['question']  # Get user input from form
    if user_input:
        # Get bot response from the model
        result = chain.invoke({"context": context, "question": user_input})
        context += f"\nUser: {user_input}\nAI: {result}"
        return render_template("response.html", question=user_input, response=result)
    return jsonify({'response': 'Error: No input provided'})

if __name__ == '__main__':
    app.run(debug=True)