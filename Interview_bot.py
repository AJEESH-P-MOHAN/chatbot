from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

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

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return ""

def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot! Say 'exit' to quit.")
    while True:
        user_input = listen()
        if user_input.lower() == "exit":
            break
        if user_input:  # If the input is not empty
            result = chain.invoke({"context": context, "question": user_input})
            print("Bot: ", result)
            speak(result)  # Convert bot response to speech
            context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
