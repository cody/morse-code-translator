#an app to translate morse code
#icon found at icons8.com

import tkinter
from tkinter import *
from playsound import playsound
from PIL import ImageTk, Image


#define window
root = tkinter.Tk()
root.title("Cody's Morse Code Translator")
root.geometry("500x350")
root.resizable(0,0)

#define fonts and colors
#using default fonts and colors for now

#define functions
def convert():
    '''call the appropriate conversion function based off radio button values'''
    #english to morse code:
    if language.get() == 1:
        getmorse()
    elif language.get() == 2:
        getenglish()

def getmorse():
    '''convert english text to morse code'''
    #string to hold morse code message
    morsecode = ""

    #get the input text and standardize it to lowercase
    text = inputtext.get("1.0", END)
    text = text.lower()

    #remove and letters or symbols not in our dict keys
    for letter in text:
        if letter not in englishtomorse.keys():
            text = text.replace(letter, "")
    #break up individual words based on space " " and put into a list
    wordlist = text.split(" ")

    #turn each individual word in word list into a leist of letters
    for word in wordlist:
        letters = list(word)
        # for each letter, get the morse code representation and append it to thew striong morse code
        for letter in letters:
            morsechar = englishtomorse[letter]
            morsecode += morsechar
            #separate individual letters with a space
            morsecode += " "
        #separte individual words with a vertical line
        morsecode += "|"

    outputtext.insert("1.0", morsecode)


def getenglish():
    '''convert a morse code message to english'''
    #string to hold english message
    english = ""
    text = inputtext.get("1.0", END)

    #remove any letters or symbols not in dict keys
    for letter in text:
        if letter not in morsetoenglish.keys():
            text = text.replace(letter, "")

    #break up each word based on vertical bar and put into a list
    wordlist = text.split("|")

    #turn each word into a list of letter
    for word in wordlist:
        letters = word.split(" ")
        #for each letter get the enligh representation and add it to the striong english
        for letter in letters:
            englishchar = morsetoenglish[letter]
            english += englishchar
        #separte individual words with a space
        english += " "

    outputtext.insert("1.0", english)

def clear():
    '''clear both text fields'''
    inputtext.delete("1.0", END)
    outputtext.delete("1.0", END)



def play():
    '''play tones based on morse code'''
    #determine where the morse code is
    if language.get() == 1:
        text = outputtext.get("1.0", END)
    elif language.get() == 2:
        text = inputtext.get("1.0", END)

    
    #play the tones (., -, " ", |)
    for value in text:
        if value == ".":
            playsound("/Users/cody/Documents/guis/morse-code-translator/dot.mp3") #macos will not allow relative file paths for some reason
            root.after(100)
        elif value == "-":
            playsound("/Users/cody/Documents/guis/morse-code-translator/dash.mp3") #using absolute filepaths until I can find a workaround
            root.after(200)
        elif value == " ":
            root.after(300)
        elif value == "|":
            root.after(700)


def showguide():
    '''show a morse code guide in a second window'''
    #image "morse" needs to be aglobal variable to put on our window
    #the window "guide" needs to be global to close in another function
    global guide
    global morse

    #create second window relative to the root window
    guide = tkinter.Toplevel()
    guide.title("Morse Guide")
    guide.geometry("350x350+"+str(root.winfo_x()+500) + "+" +str(root.winfo_y()))

    #create the image label and pack it all
    morse = ImageTk.PhotoImage(Image.open("/Users/cody/Documents/guis/morse-code-translator/morse_chart.JPG"))
    label = tkinter.Label(guide, image=morse)
    label.pack(padx=10, pady=(0,10), ipadx=5, ipady=5)

    #create close button
    closebutton = tkinter.Button(guide, text="Close", command=hideguide)
    closebutton.pack(padx=10, ipadx=50)

    #disable the guide button
    guidebutton.config(state=DISABLED)


def hideguide():
    '''hide the guide window'''
    guidebutton.config(state=NORMAL)
    guide.destroy()




#create our morse coee dictionaries
englishtomorse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
'y': '-.--', 'z': '--..', '1': '.----',
'2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.',
'0': '-----', ' ':' ', '|':'|', "":""}

morsetoenglish = dict([(value, key) for key, value in englishtomorse.items()])


#define the layout
#create frames
inputframe = tkinter.LabelFrame(root)
outputframe = tkinter.LabelFrame(root)
inputframe.pack(padx=16, pady=(16, 8))
outputframe.pack(padx=16, pady=(8, 16))

#layout for the input frame
inputtext = tkinter.Text(inputframe, height=8, width=30)
inputtext.grid(row=0, column=1, rowspan=3, padx=5, pady=5)


language = IntVar()
language.set(1)
morsebutton = tkinter.Radiobutton(inputframe, text="English --> Morse Code", variable=language, value=1)
englishbutton = tkinter.Radiobutton(inputframe, text="Morse Code --> English", variable=language, value=2)
guidebutton = tkinter.Button(inputframe, text="Guide", command=showguide)
morsebutton.grid(row=0, column=0, pady=(15, 0))
englishbutton.grid(row=1, column=0)
guidebutton.grid(row=2, column=0, sticky="WE", padx=10, ipadx=55) #had to add an ipadx value to get tkinter to display the same on macos as it does on the instructor's window laptop

#layout for the output frame
outputtext = tkinter.Text(outputframe, height=8, width=30)
outputtext.grid(row=0, column=1, rowspan=4, padx=5, pady=5)
#create buttons for the output frame
convertbutton = tkinter.Button(outputframe, text="Convert", command=convert) #Convert button ipadx defines column
playbutton = tkinter.Button(outputframe, text="Play Morse", command=play)
clearbutton = tkinter.Button(outputframe, text="Clear", command=clear)
quitbutton = tkinter.Button(outputframe, text="Quit", command=root.destroy)
#place above buttons on output frame
convertbutton.grid(row=0, column=0, padx=10, ipadx=50)
playbutton.grid(row=1, column=0, padx=10, sticky="WE")
clearbutton.grid(row=2, column=0, padx=10, sticky="WE")
quitbutton.grid(row=3, column=0, padx=10, sticky="WE")





#run the root windows main loop
root.mainloop()