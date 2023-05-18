import requests
import pyttsx3
import speech_recognition as sr
import streamlit as st
import sys
def main():
    r = sr.Recognizer()
    mic = sr.Microphone()

    engine = pyttsx3.init()
    engine.setProperty('rate', 175)

    def text_to_speech(text):
        engine.say(text)
        engine.runAndWait()


    if st.button("Tell me a joke"):  
        response = requests.get('https://icanhazdadjoke.com', headers={'Accept':'application/json'})
        joke = response.json()['joke']
        st.write(joke)  
        text_to_speech(joke)  
    
   	


    
if __name__ == "__main__":
    main()

