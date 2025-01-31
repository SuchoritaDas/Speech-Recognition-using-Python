#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install SpeechRecognition PyAudio


# In[4]:


import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()
# Function to capture and recognize speech
def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
# Use the default microphone as the audio source
mic = sr.Microphone()
# Call the function
recognize_speech_from_mic(r, mic)


# In[ ]:




