# <p style="text-align: center;">**Projeto Jarvis** :robot: </p>

<br></br>

## *Informações sobre o autor* :construction_worker:
---
---

* **Nome**: Arthur Nazário da Costa

* **Idade**: 20 anos

* **Universidade**: Universidade Federal de Uberlândia (UFU), campus Patos de Minas 

* **Graduação**: Engenharia Eletrônica e de Telecomunicações

* **Período**: 3º Período

* **Informações adicionais**: Trabalhando na Inovatos Consultoria Júnior como Gerente de Projetos e Estagiando como monitor de robótica no Colégio Nossa Senhora das Graças em Patos de Minas.

* **Objetivos de carreira**: Atuar como Cientista de Dados na área da eletrônica, desenvolver placas eletrônicas, trabalhar com banco de dados e com as linguagens Python, Java e C#.

<br/><br/>

## *Sobre o projeto* :open_file_folder:
---
---
<p style="text-align: justify;">O Projeto Jarvis ainda está na fase inicial. Assim, tentarei manté-lo atualizado à medida do possível a fim de ajudá-los com algum código que possam utilizar em alguns de seus projetos.</p>
<p style="text-align: justify;">Futuramente pretendo implementar Deep Learning para fazer o Jarvis identificar diversos padrões de ordenação, e mais funções que possam tornar a vida do pessoal mais fácil.</p>
<p style="text-align: justify;">O Jarvis pode lhe informar a hora e a data local, pesquisar vídeos no Youtube, fazer pesquisas na wikipedia sobre celebridades, cientístas e dentre outros assuntos, e contar piadas.</p>
<p style="text-align: justify;">O projeto aborda diversos conceitos como Machine Learning:robot_face:, reconhecimento de voz:microphone:, data e hora:clock12:, código limpo (talvez o código não esteja tão limpo assim :joy:), tradução de texto:speaker: e Programação Orientada a Objetos:package:.</p>

<br/><br/>

## *Bibliotecas* :book:
---
---
:pushpin: [speech_recognition](https://pypi.org/project/SpeechRecognition/ "speech_recognition")

:pushpin: [pyttsx3](https://pypi.org/project/pyttsx3/ "pyttsx3")

:pushpin: [datetime](https://docs.python.org/3/library/datetime.html "datetime")

:pushpin: [pywhatkit](https://pypi.org/project/pywhatkit/ "pywhatkit")

:pushpin: [pyjokes](https://pyjok.es/ "pyjokes")

:pushpin: [wikipedia](https://pypi.org/project/wikipedia/ "wikipedia")

:pushpin: [googletrans](https://pypi.org/project/googletrans/ "googletrans")

<br/><br/>

## *Objetivos* :dart:
---
---
:white_check_mark: Aprimorar conhecimentos e habilidades sobre a linguagem Python

:white_check_mark: Aplicar Deep Learning (Futuramente)

:white_check_mark: Fazer o Jarvis identificar vários padrões de comandos de voz

:white_check_mark: Realizar tarefas simples como informar data e hora, acessar o Youtube e pesquisar na wikipédia

:white_check_mark: Aprimorar habilidades no Git e GitHub

:white_check_mark: Apoiar a comunidade dev

<br></br>

## *Implementações* :heavy_plus_sign:
---
---

:heavy_check_mark: Versão teste

:heavy_check_mark: Comandos de informar data e hora

:heavy_check_mark: Acesso ao Youtube e pesquisa na wikipédia

:heavy_check_mark: Piadas prontas

:heavy_check_mark: Cumprimentos como bom dia, boa tarde e boa noite

<br></br>

## *Código* :computer:
---
---

<br></br>

### ***Jarvis Class*** :robot:
---
~~~python
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
        
~~~
---

*Observação:*<p style="text-align: justify">Leia o código com bastante calma para melhor interpretá-lo. É possível percerber que o Jarvis **capta somente algumas palavras chaves** para identificar qual(is) comando(s) terá que executar.</p>

<br></br>

## *Contatos* :telephone_receiver:
---
---
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/arthur-naz%C3%A1rio-da-costa-6478601a1/ "Arthur Nazário da Costa")

:email: arthurnazariodacosta@gmail.com

:iphone: +55 (34) 99691-1251
