import speech_recognition as sr
import webbrowser
import pyttsx3
from gtts import gTTS
import os
import pygame
import pyautogui
from time import sleep

class voice_assistant:
  # Initialize recognizer
  recognizer = sr.Recognizer()
  engine = pyttsx3.init()

  def record_audio(self):
    """
    Records audio from the microphone.
    """
    with sr.Microphone() as source:
      print("Speak...")
      self.recognizer.adjust_for_ambient_noise(source)
      audio = self.recognizer.listen(source)
    return audio

  def recognize_speech(self,audio):
    
    """
    Recognizes speech from the recorded audio.
    """
    try:
      text = self.recognizer.recognize_google(audio, language='en')
      print("You said: " + text)  
      return text
    except sr.UnknownValueError:
      print("Sorry, I could not understand audio")
    except sr.RequestError:
      print("Could not request results from Google Speech Recognition service")
  
  def Auto_gui(self):
    webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
    sleep(4)
    pyautogui.moveTo(200, 200, duration=1)
    pyautogui.click()
    pyautogui.moveTo(225, 225, duration=0.2)
    pyautogui.click()
          


# Alexa talk
mytext = 'Hello, what do you need?'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("session4/output.mp3")
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("session4/output.mp3")
sound.play()
while pygame.mixer.get_busy():
    pygame.time.wait(100)  # Wait 100 milliseconds
pygame.quit()

# Record speech
x=voice_assistant()
audio=x.record_audio()

# Recognize the recorded speech
text=x.recognize_speech(audio)

# execute the recognized speech
if text=="open Google":
  webbrowser.open_new_tab("https://www.google.com/")
elif text=="open Facebook":
  webbrowser.open_new_tab("https://www.facebook.com/") 
elif text=="read emails":
  x.Auto_gui()
else:
  print("not found")


