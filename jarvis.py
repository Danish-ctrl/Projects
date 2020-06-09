import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hours=int(datetime.datetime.now().hour)
    if(hours>0 and hours<12):
        engine.say('good morning danish')
    elif(hours>12 and hours<18):
        engine.say('good aftrnoon danish')
    else:
        engine.say('good eveng danish')
    
    speak('this is ur assisatnt ,how may i help u ?')

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('I am Listening. . . ')
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print('Recognizing . . ')
        query=r.recognize_google(audio, language='en-in')
        print(f'You said {query}\n')
    
    except Exception as e:
        print(e)
        print('Can You please speak again ?')
        return 'None'
    
    return query








if __name__ == "__main__":
    #speak('danish is a good boy')
    wishMe()
    while(True):
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching. . .')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=2)
            speak('According to wiki ')
            speak(result)
    

