import speech_recognition as sr  
import pyttsx3
import webbrowser
import musicLibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import time

recognizer = sr.Recognizer()  
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)  
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()  # Release the file

    # Debugging information
    print("Playback stopped. Attempting to remove file...")
    
    # Ensure the file is no longer being used before attempting to delete it
    time.sleep(1)  # Small delay to ensure the file is no longer in use
    
    try:
        if os.path.exists("temp.mp3"):
            os.remove("temp.mp3")
            print("File removed successfully.")
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"Error removing file: {e}")

def aiprocess(command):
    client = OpenAI(api_key="YOUR_API_KEY_HERE")

    completion = client.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Max, skilled in general tasks like Alexa and Google. Give short responses."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].text

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")  

    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com") 

    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")   

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in the library.")
    else:
        output = aiprocess(c)
        speak(output)

if __name__ == "__main__":  
    speak("Initializing Max...")

    while True:
        # listen for the word "Max" 
        r = sr.Recognizer()
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
            word = r.recognize_google(audio)  
            if word.lower() == "Max":
                speak("Yes?")
                # listen to command
                with sr.Microphone() as source:
                    print("Max Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)

        except Exception as e:
            print("Error: {0}".format(e))
