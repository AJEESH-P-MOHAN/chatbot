import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()
print("Hello, Iam sara how can i assist you today")
while True:
    # Use the microphone as the source
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            if text == "what is your name":
                print("my name is sara")
            elif text=="what is your age":
                print("iam a ai")
            elif text=="stop":
                break
            # print("You said: " + text)
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
        