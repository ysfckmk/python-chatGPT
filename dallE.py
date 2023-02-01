import openai
import speech_recognition as sr
import os
openai.api_key = your-api-key




def speechToText():
    # obtain audio from the microphone
  r = sr.Recognizer()
  with sr.Microphone() as source:
      print("Say something!")
      audio = r.listen(source)



  return(str(r.recognize_google(audio)))


def generateImage(sImagine):

    response = openai.Image.create(
    prompt=sImagine,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)
    return image_url
