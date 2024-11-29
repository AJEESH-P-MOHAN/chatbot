import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set properties for the text-to-speech engine
engine.setProperty('rate', 170)    # Increase speed
engine.setProperty('volume', 1.0)  # Max volume

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Initial greeting
speak("Hello! How can I assist you today?")

while True:
    # Use the microphone as the source
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Shorter adjustment time
        print("Listening...")
        audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)  # Set time limits

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")
            
            if "what is your name" in text:
                response = """My name is sara. I am an AI chatbot model.
                iam here to help you"""
            elif "hello" in text:
                response = "Hello, how can I assist you today?"
            elif "do you remember my project" in text:
                response = ("Yes, I remember you’re working on a voicebot project. You’re focusing on creating a "
                            "chatbot that can interact with students as an interviewer. "
                            "You’ve been working on integrating voice-to-text and text-to-voice conversion, "
                            "and you’re also considering using OpenAI for generating responses. "
                            "Is there anything specific you need help with regarding your project?")
            elif "goodbye" in text or "bye" in text:
                response = "Thank you. Have a nice day!"
                speak(response)
                break
            else:
                response = "I didn't catch that. Could you please repeat?"

            print(response)
            speak(response)

        except sr.UnknownValueError:
            response = "Sorry, I didn't understand that."
            print(response)
            speak(response)
        except sr.RequestError as e:
            response = f"Could not request results from Google Web Speech API; {e}"
            print(response)
            speak(response)
