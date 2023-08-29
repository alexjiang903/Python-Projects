BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random


#Image files:
window = Tk()
flashcard_image = PhotoImage(file="images/card_front.png")
backside = PhotoImage(file="images/card_back.png")
correct_image = PhotoImage(file="images/right.png")
incorrect_image = PhotoImage(file="images/wrong.png")

#Reading csv data:
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/japanese_english_romanji.csv")
finally:
    data_frame = pandas.DataFrame(data)
    to_learn = data_frame.to_dict(orient="records")


#Functions
current_card = {}

def reset():
    canvas.itemconfig(frontside, image=flashcard_image)
    canvas.itemconfig(card_title, fill="black")
    canvas.itemconfig(card_text, fill="black")


def cycle_next():
    global current_card
    reset()
    current_card = random.choice(to_learn)
    japanese_word = current_card["Japanese"]
    romanji_word = current_card["Romanji"]

    canvas.itemconfig(card_title, text="Japanese")
    canvas.itemconfig(card_text, text=japanese_word)
    canvas.itemconfig(card_text_rom, text=romanji_word)
    window.after(4000, func=card_flip)


def card_flip():
    global current_card
    english_word = current_card["English"]
    canvas.itemconfig(frontside, image=backside)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=english_word, fill="white")
    canvas.itemconfig(card_text_rom, text="")
    window.after_cancel(cycle_next)


def save_to_csv():
    global current_card
    to_learn.remove(current_card)
    data_frame = pandas.DataFrame(to_learn, columns=["Japanese", "Romanji", "English"])
    data_frame.to_csv("vocabulary_to_learn/words_to_learn.csv", index=False)
    cycle_next()




    

#Window set-up:
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

correct_button = Button(image=correct_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=save_to_csv)
correct_button.grid(row=1, column=1)
incorrect_button = Button(image=incorrect_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=cycle_next)
incorrect_button.grid(row=1, column=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
frontside = canvas.create_image(400,263,image=flashcard_image)
canvas.grid(row=0, column=0, columnspan=2)


card_title = canvas.create_text(400, 150,text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="Click the x to start!", font=("Ariel", 70, "bold"))
card_text_rom = canvas.create_text(400, 390, text="", font=("Ariel", 45, "italic"))







window.mainloop()