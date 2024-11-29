import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 160)    # Speed (words per minute)
# engine.setProperty('volume', 0.5)  # Volume (0.0 to 1.0)

# Text to be converted to speech
text = "Hello, how are you today?"

# Convert text to speech
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()
