import speech_recognition as sr
from gtts import gTTS 
from playsound import playsound
from datetime import datetime
from io import BytesIO
import pyttsx3  

r = sr.Recognizer()

def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 

with sr.Microphone() as source: 
	playsound("./signal.mp3") #ส่งสัญญาณเตือน
	audio = r.record(source, duration=6) #บันทึกเสียง 6 วินาที
	playsound("./signal.mp3") #ส่งสัญญาณเตือน
	
	try:
		text = r.recognize_google(audio, language="en") #ส่งไปให้google cloud
		MyText = text.lower() #https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/
		print("Did you say "+MyText) 
		f = open("./input.txt","w+")
		f.write(MyText)
		f.close()
		if "hello" in text:
			text = text.replace("hello", "hey how are you")
		if "what time is it" in text:
			now = datetime.now() #รับค่าเวลาขณะนั้น
			text = text.replace("what time is it", now.strftime("it is %H and %M minutes %S seconds"))
		f = open("./answer.txt","w+")
		f.write(text)
		f.close()
	except:
		text = "Sorry"
	tts = gTTS(text, lang="en") #ส่งไปให้google cloud
	tts.save("./answer.mp3") #บันทึกเสียงที่ได้จากgoogle cloud
	playsound("./answer.mp3")
