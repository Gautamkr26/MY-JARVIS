import datetime
import os
from winsound import PlaySound
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import subprocess
import pyjokes
import pywhatkit
from time import sleep
import pyautogui
import sys
import playsound as ps
import keyboard
from keyboard import press
from pynput.keyboard import Key,Controller
keyboard=Controller()
import openai
import pyttsx3

# Set up OpenAI API credentials
openai.api_key = "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"


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 200
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-us')
    except Exception as e:
        print(e)
        return "---"
    return query


def time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(time)
    print(time)


def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    print(day, month, year)
    speak(day)
    speak(month)
    speak(year)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")
    else:
        speak("Good Evening Sir!")
  


# Open chrome/website
def open_chrome():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path)
    speak("what should i search?")


def open_chatgpt():
    url = "https://chat.openai.com/chat"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)



if __name__ == "__main__":
    wishMe()
    while True:
        print('Please say the activation word')
        speak('Please say the activation word')
        query = takeCommand().lower()
        if 'jarvis' in query or 'wake up jarvis' in query:
            print('ACTIVATING JARVIS')
            speak('ACTIVATING JARVIS')
            speak("I am Jarvis")
            speak('how may i help you sir')


        while True:
            query = takeCommand().lower()
            print(query)

            if "thanks" in query:
                speak("its my pleasure sir")
            
            if 'love you 3000' in query:
                speak('activating system shortly')
            
            if 'are you their' in query:
                speak('At your service sir.')
            
            if 'hello' in query:
                speak('hye sir')
            
            if 'bye' in query:
                speak('bbye sir take care')
            
            if 'are you single' in query:
                speak('I am in a relationship with wifi')
            
            if 'who invented you' in query:
                speak('Mr Gautam sir is my master')
            
            if "time" in query:
                time()
            
            if "date" in query:
                date()    
            
            if "type" in query:
                query = query.replace("type", "")
                query = query.replace("search", "")
                keyboard.type(query)
                press('enter')

            

            # open chrome&GPT
            elif "open chrome" in query:
                open_chrome()
            elif "open chat gpt" in query:
                open_chatgpt()
            
            
             #playsound 
            elif "introduce yourself" in query:
                ps.playsound('C:\\Users\\Gautam\\OneDrive\\Desktop\\My Projects\\my jarvis\\jarvis.mp3')
            
            
            
            
            # Wikipedia search
            elif "wikipedia" in query:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)

            # Chrome search
            # elif "search" in query:
            #     speak("what should i search?")
            #     chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            #     search = takeCommand().lower()
            #     wb.get(chromepath).open_new_tab(search )
            if "search" in query:
                query = query.replace("search", "")
                speak('searching...' + query)
                pywhatkit.search(query)

            elif "play" in query:
                query = query.replace("play", "")
                speak('playing ' + query + "on youtube")
                pywhatkit.playonyt(query)

            # Launch software
            elif "open notepad" in query:
                speak("opening notepad")
                location = "C:/WINDOWS/system32/notepad.exe"
                notepad = subprocess.Popen(location)

            elif "close notepad" in query:
                speak("closing notepad")
                notepad.terminate()

            elif "vs code" in query:
                speak("opening vs code")
                location = "C:/Users/Gautam/AppData/Local\Programs/Microsoft VS Code/Code.exe"
                vs = subprocess.Popen(location)
            elif "github" in query:
                speak("opening git hub")
                location = "C:/Users/Gautam/AppData/RoamingMicrosoft/Windows/Start Menu/Programs/GitHub, Inc.exe"
                vs = subprocess.Popen(location)

            # Random jokes
            elif "joke" in query:
                speak(pyjokes.get_jokes())

            #Shutdown/Restart
            
            elif "shutdown" in query:
                speak('shutting down in 5 second')
                sleep(5)
                os.system("shutdown /s /t 1")

            elif "restart" in query:
                speak('restarting in 5 second')
                sleep(5)
                os.system("shutdown /r /t 1")
            
               
             #comands
            
            if 'open chrome' in query:
                os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
            elif 'maximize this window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('x')
            elif 'google search' in query:
                query = query.replace("google search", "")
                pyautogui.hotkey('alt', 'd')
                pyautogui.write(f"{query}", 0.1)
                pyautogui.press('enter')
            elif 'youtube search' in query:
                query = query.replace("youtube search", "")
                pyautogui.hotkey('alt', 'd')
                time.sleep(1)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.write(f"{query}", 0.1)
                pyautogui.press('enter')
            elif 'open new window' in query:
                pyautogui.hotkey('ctrl', 'n')
            elif 'open incognito window' in query:
                pyautogui.hotkey('ctrl', 'shift', 'n')
            elif 'minimise this window' in query:
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('n')
            elif 'open history' in query:
                pyautogui.hotkey('ctrl', 'h')
            elif 'open downloads' in query:
                pyautogui.hotkey('ctrl', 'j')
            elif 'previous tab' in query:
                pyautogui.hotkey('ctrl', 'shift', 'tab')
            elif 'next tab' in query:
                pyautogui.hotkey('ctrl', 'tab')
            elif 'close tab' in query:
                pyautogui.hotkey('ctrl', 'w')
            elif 'close window' in query:
                pyautogui.hotkey('ctrl', 'shift', 'w')
            elif 'clear browsing history' in query:
                pyautogui.hotkey('ctrl', 'shift', 'delete')
            elif 'close chrome' in query:
                os.system("taskkill /f /im chrome.exe")
            
            elif "volume up" in query:
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
            elif "volume down" in query:
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
            elif "mute" in query:
                pyautogui.press("volumemute")
            elif "refresh" in query:
                pyautogui.moveTo(1551, 551, 2)
                pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
                pyautogui.moveTo(1620, 667, 1)
                pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
            elif "scroll down" in query:
                pyautogui.scroll(1000)
            elif "drag visual studio to the right" in query:
                pyautogui.moveTo(46, 31, 2)
                pyautogui.dragRel(1857, 31, 2)
                

            elif "hidden menu" in query:
                pyautogui.hotkey('winleft', 'x')

            elif "task manager" in query:
                pyautogui.hotkey('ctrl', 'shift', 'esc')

            elif "task view" in query:
                pyautogui.hotkey('winleft', 'tab')

            elif "take a screenshot" in query:
                pyautogui.hotkey('winleft', 'prtscr')
                speak("done")

            elif "close the app" in query:
                pyautogui.hotkey('alt', 'f4')
                speak("done")

            elif "setting" in query:
                pyautogui.hotkey('winleft', 'i')

            elif "new virtual desktop" in query:
                pyautogui.hotkey('winleft', 'ctrl', 'd')

            elif "lock screen" in query:
                pyautogui.hotkey('winleft', 'l')

            elif "this pc" in query:
                pyautogui.hotkey('winleft', 'e')

            elif "back" in query:
                pyautogui.hotkey('esc')

            elif "minimise" in query:
                pyautogui.hotkey('winleft', 'm')

            elif "restore" in query:
                pyautogui.hotkey('winleft', 'shift', 'm')

            elif "switch app" in query:
                pyautogui.hotkey('alt', 'tab')

            elif "upside" in query:
                pyautogui.hotkey('pgup')

            elif "downside" in query:
                pyautogui.hotkey('pgdn')

            elif "enter" in query:
                pyautogui.hotkey('enter')
            
            elif "full screen" in query:
                pyautogui.hotkey('f')
            
            elif "short screen" in query:
                pyautogui.hotkey('f')

            elif "quit" in query:
                speak("thanks for using me sir, take care")
                sys.exit()
            elif 'activate gpt' in query:
                speak('ACTIVATING CHAT GPT')
                while True:
                    print("Ask Chat GPT")
                    speak("Ask Chat GPT")
                    # # prompt=takeCommand().lower()
                    # model_engine="text-davinci-003"
                    # # prompt=input('Ask JARVIS...')
                    # # keyboard.type(prompt)
                    # prompt=takeCommand().lower()
                    # # prompt==a
                    # if 'exit' in prompt or 'quit' in prompt:
                    #     break
                    # completion=openai.Completion.create(
                    # engine=model_engine,
                    # prompt=prompt,
                    # max_tokens=1024,
                    # n=1, stop=None,
                    # temperature=0.5
                    # )
                    # response=completion.choices[0].text
                    # print(response)
                    # query=takeCommand().lower()
                    # if 'speak' in query:
                    #     speak(response)
                    
                    user_input = input("User: ")
                    response = openai.Completion.create(
                    engine='text-davinci-003',
                    prompt=f"You: {user_input}\nAssistant:",
                    max_tokens=50,
                    temperature=0.7,
                    n=1,
                    stop=None,
                    )
                    print("Assistant:", response.choices[0].text.strip())
