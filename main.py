from tkinter import *
from translator import *
from playsound import playsound
import matplotlib.pyplot as plt
import pyperclip


#functions for copy button to bind to
def copyMorse():
    pyperclip.copy(morseVar.get())

def copyText():
    pyperclip.copy(textVar.get())



def plotFrequency():
    morse = morseVar.get()
    data = frequencyAnalysis(morse)

    if not data: #checks if the returned tupple actually has anything inside, if not just does not open a new window
        return

    symbols = list(data.keys())
    counts = list(data.values())

    plt.figure(figsize=(10, 5))
    plt.bar(symbols, counts, color='yellow', edgecolor='black')
    plt.title('Morse Code Frequency')
    plt.xlabel('Symbol')
    plt.ylabel('Count')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

#function to play back sound from the morse code text box
def sound():
    for i in morseVar.get():
        if i == '.':
            playsound("dot.mp3")
        elif i == '-':
            playsound("dash.mp3")

        elif i == ' ':
            playsound("space.mp3")
        else:
            playsound("wordBreak.mp3")

#function has placeholder values cus when called, it has 3 passed arguments that need to go somewhere? compiler dum dum no big suprise
def update_translation(a, b, c): # function that updates the opposite textbox with a translation from plain text to morse or vice versa

    focus = root.focus_get() #object is compared to currently focused UI element to figure out which text box is being edited/ what needs to be updated

    if focus == morseEntry:#updates plane text
        morseText = morseVar.get()
        plainTtext = morse_to_text(morseText)
        textVar.set(plainTtext)
    else:#default case, updates morse code
        plainTtext = textVar.get()
        morseText = textToMorse(plainTtext)
        morseVar.set(morseText) 


#setting up GUI
root = Tk()
root.title("Text to Morse")
root.geometry("400x250")
root.configure(bg='black')

#object to store our background
bg = PhotoImage(file = "background.png") 

#drawing the background onto the canvas, using place to keep it behind the rest of the objects
canvas1 = Canvas(root, width=400, height=300, highlightthickness=0)
canvas1.place(x=0, y=0, relwidth=1, relheight=1)
canvas1.create_image(0, 0, image=bg, anchor="nw")

#initializing some variables to track for the entries
textVar = StringVar()
morseVar = StringVar()

#drawing out the text IO
label1 = Label(root, text="Text:", bg='black', fg='yellow')
label1.pack(pady=10)
textEntry = Entry(root, textvariable=textVar)
textEntry.pack(pady=10)

#drawing out the morse IO
label2 = Label(root, text="Morse:", bg='black', fg='yellow')
label2.pack(pady=10)
morseEntry = Entry(root, textvariable=morseVar)
morseEntry.pack(pady=10)

#play button calls the sound function to allow user to hear morse code
enterButton = Button(root, text="▶️",justify="center", bg="yellow", fg="black", width=3, command=sound)
enterButton.pack(pady=15)

#graph button to open the frequency analyzer 
graphing = Button(root, text="📊 Frequency", bg="yellow", fg="black", command=plotFrequency)
graphing.pack(pady=5)

#tracking changes to text & morse variables to call our update function ONLY when we change inputs
textVar.trace_add("write", update_translation)
morseVar.trace_add("write", update_translation)



root.mainloop()
