from tkinter import *

import tkinter.simpledialog

import threading

try:
    from PIL import ImageTk, Image
except:
    print("Python PIL package not found. Please install it to be able load images correctly.")
import random
import re

dice_num = 0

SNAKE_HOLES = [98,78,81,74,62,58,48, 44, 39, 34, 28, 13]

LADDER_BRIDGES = [3, 8, 6, 26, 14, 22, 32, 49,54,64,76,83,86,95]
player_1_pos = 0

player_moves = 0

player_bites = 0

player_climb = 0

player_name = ""

time_elapsed = 0
p=""


def randomColor():
    global PlayerMovesLabel
    COLORS = ['red', 'blue', 'yellow', 'pink', 'lightblue', 'steel blue', 'turquoise', 'sandy brown', 'purple',
              'violet red', 'violet', 'maroon', 'tomato', 'orange', 'green yellow','indigo']
    randomColor = random.randint(0, len(COLORS))
    PlayerMovesLabel.config(bg=COLORS[randomColor])


def colorCycle():
    global PlayerMovesLabel, time_elapsed

    try:
        mytimer = threading.Timer(0.2, colorCycle)
        mytimer.daemon = True
        mytimer.start()

        if player_1_pos == 100:
            randomColor()
        else:
            PlayerMovesLabel.config(bg='white')

        time_elapsed = time_elapsed + 1
    except:
        return


def movePlayer():
    global player_1_pos
    global dice_num
    global player_moves
    global player_bites
    global player_climb
    global grid_array
    global PlayerMovesLabel
    global diceRollLabel
    global time_elapsed

    if player_1_pos == 100:
        player_1_pos = 0
        player_moves = 0
        player_1_pos = 0
        player_bites = 0
        player_climb = 0
        grid_array[100 - 1].config(bg="white")
        time_elapsed = 0

    old_player_pos = player_1_pos
    new_player_pos = player_1_pos + dice_num

    additional_message = ""

    if new_player_pos > 100:
        new_player_pos = 100 - (new_player_pos - 100)

    
    for idx, val in enumerate(SNAKE_HOLES):
        if idx % 2 == 0:

            if new_player_pos == SNAKE_HOLES[idx]:

                new_player_pos = SNAKE_HOLES[idx + 1]
                player_bites = player_bites + 1
                additional_message = "Bitten | "

    
    for idx, val in enumerate(LADDER_BRIDGES):
        if idx % 2 == 0:

            if new_player_pos == LADDER_BRIDGES[idx]:

                new_player_pos = LADDER_BRIDGES[idx + 1]
                player_climb = player_climb + 1
                additional_message = "Climb | "

    if old_player_pos > 0:
        grid_array[old_player_pos - 1].config(bg="white")

    grid_array[new_player_pos - 1].config(bg="yellow")

    player_1_pos = new_player_pos
    player_moves = player_moves + 1

    if player_1_pos == 100:
        PlayerMovesLabel['text'] = "*WON* Move: " + str(player_moves) + ", Bite: " + str(
            player_bites) + ", Climb:" + str(player_climb) + " *WON*"
        tkinter.messagebox.showinfo("*WON*",
                                    player_name + " Won the game in " + str(player_moves) + " moves during " + str(
                                        int(time_elapsed / 5)) + " seconds!")
    else:
        PlayerMovesLabel['text'] = additional_message + "Move: " + str(player_moves) + ", Bite: " + str(
            player_bites) + ", Climb:" + str(player_climb)


def rollTheDice():
    global dice_num
    global diceRollLabel
    dice_num = random.randint(1, 6)
    diceRollLabel['text'] = player_name + " Rolled: " + str(dice_num)
    movePlayer()


def createGUI():
    global grid_array
    global PlayerMovesLabel
    global diceRollLabel
    global diceWindow
    global player_name
    global p
    pattern=r".*"

    diceWindow = Tk()

    diceWindow.title("SNAKE & LADDERS")

    diceWindow.resizable(width=False, height=False)
    diceWindow.config(bg='white')

    RevertLogoImage = Label(diceWindow, text="Snake & Ladder", bg='white', font=("Arial", 30))
    RevertLogoImage.grid(row=0, column=1, columnspan=10)

    PlayerMovesLabel = Label(diceWindow, text="Please enter your name in popup window", bg='white')
    PlayerMovesLabel.grid(row=1, column=1, columnspan=10)

    btnRoll = Button(diceWindow, text="Roll", command=rollTheDice, width=30)
    btnRoll.grid(row=3, column=1, columnspan=10)

    grid_array = []
    for y in range(0, 10):
        for x in range(0, 10):
            array_num = ((x + 1) + (y * 10))
            grid_array.append(Label(diceWindow, borderwidth=8, text=array_num))

            xx = x
            yy = y

            yy = abs(yy - 10)
            if not yy % 2:
                xx = abs(xx - 9)

            grid_array[array_num - 1].grid(row=(yy + 1) + 4, column=(xx + 1))
            grid_array[array_num - 1].config(bg='white')
            if array_num in SNAKE_HOLES:

                if SNAKE_HOLES.index(array_num) % 2 == 0:
                    grid_array[array_num - 1].config(fg="red")
                else:
                    grid_array[array_num - 1].config(fg="orange")

            if array_num in LADDER_BRIDGES:

                if LADDER_BRIDGES.index(array_num) % 2 == 0:
                    grid_array[array_num - 1].config(fg="blue")
                else:
                    grid_array[array_num - 1].config(fg="lightblue")
    colorCycle()

    if re.match(pattern,player_name):
        p=player_name
        player_name = tkinter.simpledialog.askstring("Player Name", "Please enter your name: ")
        PlayerMovesLabel['text'] = '- Waiting for first Roll -'


    diceRollLabel = Label(diceWindow, bg="white", text="Welcome " + player_name + ", Please roll your dice!")
    diceRollLabel.grid(row=2, column=1, columnspan=10)

    diceWindow.mainloop()

GUI = threading.Thread(target=createGUI())
GUI.start()
q=player_moves
Process = threading.Thread(target=createGUI())
Process.start()
w=player_moves

GUI.join()
Process.join()

if q<w:
    tkinter.messagebox.showinfo("*WON*",
                               p + " Won the game by " + str(w-q) + " moves")
else:
    tkinter.messagebox.showinfo("*WON*",
                                player_name + " Won the game by " + str(q-w) + " moves")