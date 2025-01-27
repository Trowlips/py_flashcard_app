import random
import tkinter
from tkinter import PhotoImage
import pandas

BACKGROUND_COLOR = "#B1DDC6"

def wrong_click():
    french_text, english_text = new_word_pair()
    update_display_text(text=french_text)

def correct_click():
    french_text, english_text =new_word_pair()
    update_display_text(text=french_text)

def new_word_pair():

    # random_pair = random.choice(french_english_dict)
    # key = next(iter(random_pair))
    # displayed_french = key
    # print(random_pair, displayed_french)
    # displayed_english = random_pair[key]

    random.shuffle(french_keys)
    random_french = random.choice(french_keys)
    print(random_french, french_english_dict[random_french])
    return random_french, french_english_dict[random_french]


def update_display_text(title="French", text=""):
    canvas.itemconfig(canvas_word, text=text)
    pass

french_words = pandas.read_csv("data/french_words.csv")
word_pair_list = french_words.to_dict(orient="records")
french_english_dict = {pair["French"]:pair["English"] for pair in word_pair_list}
french_keys = list(iter(french_english_dict))
starting_french = random.choice(french_keys)

# ====================================UI=========================================
# Window
window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
correct_image = PhotoImage(file="images/right.png")

# Flash Card
canvas = tkinter.Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 265, image=front_card_image)

canvas_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text=starting_french, font=("Ariel", 60, "bold"))


# Button
wrong_btn =tkinter.Button(image=wrong_image, highlightthickness=0, command=wrong_click)
correct_btn = tkinter.Button(image=correct_image, highlightthickness=0, command=correct_click)


# Grid
canvas.grid(column=0, row=0, columnspan=2)
wrong_btn.grid(column=0, row=1)
correct_btn.grid(column=1, row=1)



window.mainloop()
