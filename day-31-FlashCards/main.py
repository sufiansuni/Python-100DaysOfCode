import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_card = None

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

to_learn_file_path = "day-31-FlashCards/data/words_to_learn.csv"
data_file_path = "day-31-FlashCards/data/japanese_words.csv"
try:
    words_dataframe = pandas.read_csv(to_learn_file_path)
except FileNotFoundError:
    words_dataframe = pandas.read_csv(data_file_path)
    words_dataframe.to_csv(to_learn_file_path, index=False)
finally:   
    words_dict = words_dataframe.to_dict(orient="records")

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = tkinter.PhotoImage(file="day-31-FlashCards/images/card_front.png")
back_img = tkinter.PhotoImage(file="day-31-FlashCards/images/card_back.png")
card = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(400, 150, text="Language", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

def flip_card():
    word_english = current_card["english"]
    canvas.itemconfigure(language_text, text="English", fill="white")
    canvas.itemconfigure(word_text, text=word_english, fill="white")
    canvas.itemconfigure(card, image=back_img)

def next_card():
    global flip_timer, current_card, words_dict
    if flip_timer != None:
            window.after_cancel(flip_timer)

    if len(words_dict) > 0:
        current_card = random.choice(words_dict)
        word_jap = current_card["japanese"]
        word_romaji = current_card["romaji"]

        canvas.itemconfigure(language_text, text="Japanese", fill="black")
        canvas.itemconfigure(word_text, text= f"{word_jap} ({word_romaji})", fill="black")
        canvas.itemconfigure(card, image=front_img)
        
        flip_timer = window.after(3000, flip_card)
    else:
        current_card = None
        canvas.itemconfigure(language_text, text="All Words Learnt", fill="black")
        canvas.itemconfigure(word_text, text="Congrats!", fill="black")
        canvas.itemconfigure(card, image=front_img)

def right_button_click():
    if current_card != None:
        words_dict.remove(current_card)
        words_dataframe = pandas.DataFrame(words_dict, columns = ["japanese", "romaji", "english"])
        words_dataframe.to_csv(to_learn_file_path, index=False)
        next_card()

wrong_image = tkinter.PhotoImage(file="day-31-FlashCards/images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="day-31-FlashCards/images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=right_button_click)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()
