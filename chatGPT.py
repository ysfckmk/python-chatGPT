import os
import openai
import pyttsx3
import speech_recognition as sr


def speechToText():
    # obtain audio from the microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
      print("Say something!")
      audio = r.listen(source)



  return(str(r.recognize_google(audio)))





def askToGpt(ask):
  # enter here your api key from https://openai.com/api/
  openai.api_key = your-api-key
  response = openai.Completion.create(
    model='text-davinci-003',
    prompt=ask,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  rspText = response['choices'][0]['text']
  engine = pyttsx3.init()
  engine.setProperty('rate', 120)    
  engine.say(rspText)
  engine.runAndWait()
  return rspText
