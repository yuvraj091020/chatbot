from chatterbot import ChatBot
import pyttsx3 as tts
from tkinter import *
from PIL import ImageTk, Image
import wikipedia
import datetime

bot = ChatBot("CoviBot")
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
    answer = wikipedia.summary(question, sentences=2)
    chatWindow.insert(END, "User : " + question)
    chatWindow.insert(END, "CoviBot : " + str(answer))
    messageWindow.delete(0, END)
    chatWindow.yview(END)
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
