
import googletrans
import speech_recognition
import gtts
import playsound

input_lang = "hi"
output_lang = "en"


reco = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:

   print("Say : ")
   aawaj = reco.listen(source)
   text = reco.recognize_google(aawaj,language=input_lang)
   print(text)
  

translator = googletrans.Translator()
translation = translator.translate(text,dest=output_lang)
print("Your input is : ",translation.text)
con_aud = gtts.gTTS(translation.text, lang = output_lang)
con_aud.save("File.mp3")
playsound.playsound("File.mp3")

