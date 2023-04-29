from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")



def next_card():
    current_card =  random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
card_word  = canvas.create_text(400,263, text="Word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button =Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1,column=1)

next_card()


window.mainloop()