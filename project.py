import turtle
import tkinter as tk
from tkinter import *
import random

def stand():
    t.goto(-50,-120)
    t.forward(100)
    t.back(50)
    t.left(90)
    t.forward(220)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)

def kill(num):
    if(num==4):
        t.penup()
        t.goto(80,30)
        t.pendown()
        t.circle(20)
    if (num==3):
        t.penup()
        t.goto(100,10)
        t.pendown()
        t.forward(40)
    if (num==2):
        t.penup()
        t.goto(100,5)
        t.pendown()
        t.goto(90,-10)
        t.penup()
        t.goto(100,5)
        t.pendown()
        t.goto(110,-10)
    if (num==1):
        t.penup()
        t.goto(100,-30)
        t.pendown()
        t.goto(90,-45)
        t.penup()
        t.goto(100,-30)
        t.pendown()
        t.goto(110,-45)



root = Tk()
root.geometry("500x500")
canvas = tk.Canvas(master = root, width = 500, height = 500)
canvas.pack()
t = turtle.RawTurtle(canvas)
t.pencolor("#ff0000") # Red
#tk.Button(master = root, text = "Draw", command = stand).pack()
Label(root, text="*** HANGMAN GAME *** ").place(x=180,y=20)
stand()
lis=["_","_","_","_","_","_","_","_","_","_"]
words=["characters", "literature", "perfection","basketball","watermelon","appreciate"]
word=random.choice(words)
count=4
Label(root, text="Word = ").place(x=200,y=450)
st = ' '.join(map(str, lis))
Label(root, text=st).place(x=250,y=450)
while(count!=0 and "_" in lis):
    yes=False
    char=tk.simpledialog.askstring("Input", "Guess a letter ")
    for i in range(10):
        if char == word[i]:
            lis[i]=char
            yes=True
    if not yes:
        kill(count)
        count-=1
    st = ' '.join(map(str, lis))
    Label(root, text=st).place(x=250,y=450)

if (count==0):
    Label(root, text="GAME OVER, YOU LOST").place(x=170,y=90)
else:
    Label(root, text="CONGRATULATIONS, YOU GUESSED THE WORD ").place(x=160,y=90)


root.mainloop()
