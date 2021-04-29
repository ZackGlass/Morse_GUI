from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Setup
led = 11
GPIO.setup(led, GPIO.OUT)


# Definitions
win = Tk()
win.title("Morse Code LED")
win.geometry("300x140+400+300")

# Dictionary containing Morse Code
# Credit for morse code dictionary code:
# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/morse_code/

MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', "'": '.----.', '(': '-.--.-', ')': '-.--.-', 
        ',': '--..--', '-': '-....-', '.': '.-.-.-', '/': '-..-.', '0': '-----', 
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ':': '---...', 
        ';': '-.-.-.', '?': '..--..', '_': '..--.-', ' ': ' '
        }
 

# Functions
def toMorse():
    inputValid = False
    input = ent.get()
    inputValid = checkInput(input)
    input = input.upper()
    try:
        if inputValid == True:
            for i in input:
                for j in MORSE[i]:
                    if j == '.':
                        dot()
                    elif j == '-':
                        dash()
                    time.sleep(0.3)
                time.sleep(0.2)
            ent.delete(0, len(input))
    except KeyError:
        win.msg.set("Error: No Corresponding Morse Code value for character")
        ent.delete(0, len(input))
            
def checkInput(input):
    valid = False
    if len(input) <= 12:
        valid = True
    else:
        win.msg.set("Error: Input must be 12 characters or less.")
    return valid

def dot():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.1)
                
def dash():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.1)
                
def close():
    GPIO.cleanup()
    win.destroy()
    
# Widgets
Label(win, text="Enter a Word").grid(row=0, column=0, padx=100, sticky=SW)
ent = Entry(win, width=30)
ent.grid(row = 1, column=0, padx=28, sticky=SW)

goButton = Button(win, text="Convert", command = toMorse, width = 10).grid(row=3, column=0, padx=22, pady=5, sticky=SW)
exitButton = Button(win, text = "Exit", command=close, width = 10).grid(row=3, column=0, padx=172, pady=5, sticky=SW)

win.msg = StringVar()
infoBox = Message(win, textvariable = win.msg, width = 250).grid(row=4, column=0, padx=20, sticky=SW)

win.protocol("WM_DELETE_WINDOW", close)

# Loop
win.mainloop()

