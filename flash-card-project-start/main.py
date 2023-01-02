from tkinter import *
import pandas
import random
global card_front_img, flip_timer

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
french_dict = {}

# Read dict:
try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    french_dict = original_data.to_dict(orient="records")
else:
    french_dict = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    french_dict.remove(current_card)
    pandas.DataFrame(french_dict)
    data.to_csv("data/to_learn.csv", index=False)
    next_card()


# Create UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Create Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)


card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#Buttons:
x_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

v_image = PhotoImage(file="images/right.png")
known_button = Button(image=v_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)


next_card()


window.mainloop()




