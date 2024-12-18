from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card_dict = {}
df ={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/spanish_words.csv")
    df = data.to_dict(orient="records")
else:
    df = data.to_dict(orient="records")


def next_word():
    global current_card_dict, flip_timer
    window.after_cancel(flip_timer)
    current_card_dict = random.choice(df)
    canvas.itemconfig(card_title,text=current_card_dict["Spanish"], fill="black")
    canvas.itemconfig(present_img, image=front_img)
    canvas.itemconfig(language, text= "Spanish", fill="black")
    flip_timer = window.after(3000, func=english)


def english():
    # To change the image:
    canvas.itemconfig(card_title,text=current_card_dict["English"], fill="#333333")
    canvas.itemconfig(present_img, image=back_img)
    canvas.itemconfig(language, text= "English", fill="#333333")


def is_known():
    df.remove(current_card_dict)
    data = pandas.DataFrame(df)
    data.to_csv("data/words_to_learn.csv",index=False)
    data = pandas.read_csv("data/words_to_learn.csv")
    next_word()


window = Tk()
window.title("Flash App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=english)
canvas = Canvas(width=800, height=526, highlightthickness=0)
back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
present_img = canvas.create_image(400,263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)
language = canvas.create_text(400, 150, text="Spanish", font=("Ariel", 40, "italic"))
card_title = canvas.create_text(400, 263, text="Spanish", font=("Ariel", 60, "bold"))


right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(window, image=wrong_img, highlightthickness=0, command=next_word)
wrong_btn.grid(row=1, column=0)
right_btn = Button(window, image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)

next_word()



window.mainloop()
