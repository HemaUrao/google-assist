import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there was an issue with the speech recognition service."

# Function to speak the response
def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")

# Main loop
while True:
    user_input = recognize_speech()
    print("You said:", user_input)
    response = "You said: " + user_input
    speak(response)