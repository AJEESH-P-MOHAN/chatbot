from flask import Flask, request, render_template, send_file, jsonify, session, url_for
import ollama
import os
from werkzeug.utils import secure_filename



app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generates a random 24-byte string


@app.route("/newchat")
def new_chat():
    # Clear the messages from the session
    session.pop('messages', None)
    return  render_template("index.html") # Redirect to the home page (chat page)


# Define a route for the home page
@app.route("/")
def index():
    return render_template("index.html")


# Define a route for handling questions (chatting)
@app.route("/chat", methods=["POST"])
def chat():
    
    try:
        
        question = request.form["question"]
        message = {
            'role': 'user',
            'content': question
        }
        
        # Use the ollama.chat function to generate a response
        res = ollama.chat(
            model="llama3.1",
            messages=[message]
        )

        # Prepare the response message
        response_message = {
            'question': question,
            'response': res['message']['content']
        }

        # Initialize the messages list in the session if it doesn't exist
        if 'messages' not in session:
            session['messages'] = []

        # Append the new question and response to the session
        session['messages'].append(response_message)
        session.modified = True  # Mark the session as modified

        # Render the response.html template with the response
        return render_template("response.html",  messages=session['messages'])
    except Exception as e:

        # Prepare the error message
        error_message = {
            'question': question,
            'response': str(e)
        }
        
        
        # Initialize the messages list in the session if it doesn't exist
        if 'messages' not in session:
            session['messages'] = []

        # Append the error message to the session
        session['messages'].append(error_message)
        session.modified = True  # Mark the session as modified

        # Render the response.html template with the error message
        return render_template("response.html", messages=session['messages'])
    


if __name__ == "__main__":
    app.run(debug=True)