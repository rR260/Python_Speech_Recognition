import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("SPEAK SOMETHING");
    audio=r.listen(source)
    print("TIME OVER,  THANKS");

try:
    print("TEXT:"+r.recognize_google(audio));
except:
    pass;
