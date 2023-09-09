import requests
import json
import pyttsx3

text_speech = pyttsx3.init()

city = input("Enter the name of the City : \n")

url = f"http://api.weatherapi.com/v1/current.json?key=d7a96ec949e841e4ae2172352230906&q={city}"

r = requests.get(url)
# print(r.text)     --> ye sb kuch print krke de dega.
# print(type(r.text))  --> ye type btayega

wdic = json.loads(r.text)
# print(wdic["current"]["temp_c"])  --> ye sirf temperature batayega
w = wdic["current"]["temp_c"]

text_speech.say(f"The current weather in {city} is {w} degrees")
text_speech.runAndWait()