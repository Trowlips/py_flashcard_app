import random
import tkinter
from tkinter import PhotoImage
import pandas

BACKGROUND_COLOR = "#B1DDC6"

def load_file():
    try:
        csv_file = pandas.read_csv("data/words_to_learn.csv")
        print("Loading Progress")
    except FileNotFoundError:
        print("No Progress yet")
        csv_file = pandas.read_csv("data/french_words.csv")

    return csv_file

def next_word(known=False):
    global timer, french_text, english_text
    window.after_cancel(timer)
    french_text, english_text = new_word_pair()
    update_display_card(title="French", text=french_text)
    timer = window.after(3000, lambda: update_display_card(title="English", text=english_text, front=False))

    if known:
        french_keys.remove(french_text)
        english_list = [french_english_dict[french] for french in french_keys]
        new_dict = {
            "French": french_keys,
            "English": english_list
        }
        learn_df = pandas.DataFrame(new_dict)
        learn_df.to_csv("data/words_to_learn.csv", index=False)

def new_word_pair():

    # random.shuffle(french_keys)
    random_french = random.choice(french_keys)
    # print(random_french, french_english_dict[random_french])
    return random_french, french_english_dict[random_french]


def update_display_card(title="French", text="", front=True):
    if front:
        canvas.itemconfig(card_image, image=front_card_image)
        canvas.itemconfig(canvas_title, fill="black")
        canvas.itemconfig(canvas_word, fill="black")
    else:
        canvas.itemconfig(card_image, image=back_card_image)
        canvas.itemconfig(canvas_title, fill="white")
        canvas.itemconfig(canvas_word, fill="white")

    canvas.itemconfig(canvas_title, text=title)
    canvas.itemconfig(canvas_word, text=text)

french_words = load_file()
word_pair_list = french_words.to_dict(orient="records")
french_english_dict = {pair["French"]:pair["English"] for pair in word_pair_list}
french_keys = list(iter(french_english_dict))

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
card_image = canvas.create_image(400, 265, image=front_card_image)

canvas_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Start", font=("Ariel", 60, "bold"))


# Button
wrong_btn =tkinter.Button(image=wrong_image, highlightthickness=0, command=lambda: next_word(False))
correct_btn = tkinter.Button(image=correct_image, highlightthickness=0, command=lambda: next_word(True))


# Grid
canvas.grid(column=0, row=0, columnspan=2)
wrong_btn.grid(column=0, row=1)
correct_btn.grid(column=1, row=1)

# Start
french_text, english_text = new_word_pair()
update_display_card(title="French", text=french_text)
timer = window.after(3000, lambda: update_display_card(title="English", text=english_text, front=False))

window.mainloop()
