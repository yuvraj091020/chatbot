from chatterbot import ChatBot
import pyttsx3 as tts
from tkinter import *
from PIL import ImageTk, Image
import wikipedia
import datetime
import requests


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


headers = {
    "apikey": "c9f2b640-ff55-11eb-a01f-055218eaec09"}

bot = ChatBot("CoviBot", tagger_language=ENGSM)
engine = tts.init()
print("You are talking to bot! \n")

root = Tk()
root.title("CoviBot")
root.configure(bg="gray94")
root.geometry("445x585")


def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty("rate", 180)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning !")
    elif 12 <= hour < 18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("I am CoviBot")


wishMe()


def bot_will_respond():
    question = messageWindow.get()
    chatWindow.insert(END, "User :" + question)
    parameters = (
        ("q", question),
    )
    answer, answer2 = "", ""
    try:
        answer2 = wikipedia.summary(question, sentences=2)
        print(answer2)
    except wikipedia.exceptions.PageError:
        print("No results found in wikipedia for:", question)

    try:
        answer = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=parameters)
        res = answer.json()['organic']
        for dta in res:
            try:
                answer = dta['description']
                break
            except Exception as e:
                print(e)
                answer = ""
        print(answer)
    except:
        answer = ""
    if answer[-3:-1] + answer[-1] == "...":
        lst = answer.split(".")
        answer = ".".join(lst[0:-3])

    if answer2 and answer:
        chatWindow.insert(END, "CoviBot :" + str(answer2))
        chatWindow.insert(END, "OR")
        chatWindow.insert(END, str(answer))
    elif not answer2 and not answer:
        chatWindow.insert(END, "CoviBot :" + "I am Sorry. You can search it on google.")
    else:
        chatWindow.insert(END, "CoviBot  :" + str(answer))
    messageWindow.delete(0, END)
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    engine.getProperty('rate')
    engine.setProperty("rate", 160)
    engine.say(str(answer))
    engine.runAndWait()


main_menu = Menu(root)
file_menu = Menu(root)
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

img = ImageTk.PhotoImage(Image.open("BOT.png"))
photoL = Label(root, image=img)
photoL.pack(pady=3)

frame = Frame(root)
scrollbar = Scrollbar(frame, relief=RIDGE, bd=5)
scrollbar2 = Scrollbar(frame, orient='horizontal', relief=RIDGE, bd=5)
chatWindow = Listbox(frame, highlightthickness=3, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set,
                     relief=RAISED, bg="gray88", fg="cyan4", width=500, height=15, font=("Bell MT", 13, "bold"))
scrollbar.pack(side=RIGHT, fill=Y, pady=4)
scrollbar2.pack(side=BOTTOM, fill=X, pady=0)
chatWindow.pack(side=LEFT, fill=BOTH, pady=4)
scrollbar.config(command=chatWindow.yview)
scrollbar2.config(command=chatWindow.xview)
chatWindow.config(highlightbackground="cyan2", highlightcolor="cyan2")
frame.pack()

frame1 = Frame(root)
Button = Button(frame1, bd=5, relief=RAISED, text="Enter", bg="light sea green", fg="black", height=1,
                activebackground="cyan4", font=("BatmanForeverAlternate", 16), command=bot_will_respond)
messageWindow = Entry(frame1, relief=GROOVE, highlightthickness=3, bg="White", fg="black", width=300,
                      font=("Bell MT", 13, "bold"))
Button.pack(side=RIGHT, fill=X, pady=4)
messageWindow.pack(side=LEFT, fill=BOTH, pady=4)
messageWindow.config(highlightbackground="cyan3", highlightcolor="cyan3")
frame1.pack()

root.mainloop()
