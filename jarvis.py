import speech_recognition as sr
from constants import *
import pyttsx3
import datetime
import pywhatkit
import pyjokes
import wikipedia as wkp
from googletrans import Translator


class Jarvis:


    def __init__(self):
        # Reconhecer a voz pelo microfone
        self.listener = sr.Recognizer()
        # Iniciar a engine onde a Alexa irá falar com o usuário
        self.engine = pyttsx3.init()
        
        # Comandos para alterar a voz do bot
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.translater = Translator()


    def catch_voice(self):
        try:
            with sr.Microphone() as source:
                while True:
                    self.first_greetings()
                    self.speak("Ouvindo...")
                    voice = self.listener.listen(source)
                    command = self.listener.recognize_google(voice, language='pt-br')
                    command = command.lower()
                    if "jarvis" in command:
                        command = command.replace('jarvis', '')
                                            
                        if 'tocar' in command:
                            song = command.replace('tocar', '')
                            self.speak(f"Tocando {song}")
                            self.play_music(command)
                        elif 'horas' in command:
                            self.get_curr_time()
                        elif 'dia' in command or 'data' in command:
                            self.get_curr_date()
                        elif 'pesquisar' in command or 'quem é' in command:
                            person = command.replace('quem é', '')
                            self.search_wiki(person)
                        elif 'piada' in command:
                            joke = self.translater.translate(pyjokes.get_joke(), dest='pt')
                            self.speak(joke.text)
                        else: 
                            self.speak("Poderia repetir por favor?")
                    elif 'finalizar' in command or 'fechar' in command:
                        self.final_greetings()
                        break
                    else:
                        self.speak('Por favor fale meu nome quando solicitar alguma coisa.')
                    
        except: pass


    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()


    def play_music(self, music):
        pywhatkit.playonyt(music)


    def get_curr_time(self):
        time = datetime.datetime.now().strftime("%I:%M:%S")
        self.speak(time)


    def get_curr_date(self):
        day = int(datetime.datetime.now().day)
        month = int(datetime.datetime.now().month)
        year = int(datetime.datetime.now().year)

        self.speak(f"Hoje é {day} de {MESES[month - 1]} de {year}")


    def search_wiki(self, person):
        info = self.translater.translate(wkp.summary(person, 1), dest='pt')
        self.speak(info.text)


    def first_greetings(self):
        hour = int(datetime.datetime.now().hour)

        if hour >= 6 and hour < 12:
            self.speak("Bom dia!")
        elif hour >= 12 and hour < 18:
            self.speak("Boa tarde!")
        elif hour >= 18 and hour < 24:
            self.speak("Boa noite!")
        else: 
            self.speak("Ola madrugadeiro!")

    
    def final_greetings(self):
        hour = int(datetime.datetime.now().hour)

        if hour >= 6 and hour < 12:
            self.speak("Tenha um bom dia.")
        elif hour >= 12 and hour < 18:
            self.speak("Tenha uma boa tarde.")
        elif hour >= 18 and hour < 24:
            self.speak("Tenha uma boa noite.")
        else: 
            self.speak("Aproveite sua madrugada e durma bem durante o dia.")
        

