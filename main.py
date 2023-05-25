import pixela_functions as pf
from tkinter import *

window = Tk()
window.title("habit-tracker")
window.config(padx=50, pady=50)

window.mainloop()

# window = Tk()
# window.title("Korean Flashcard App")
# window.config(padx=50, pady=50, bg="#B1DDC6")

# canvas = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6", highlightbackground="#B1DDC6")
# card_front_img = PhotoImage(file="images/card_front.png")
# card_back_img = PhotoImage(file="images/card_back.png")
# card = canvas.create_image(400, 263, image=card_front_img)
# canvas.grid(row=0, column=0, columnspan=2)

# checkmark_img = PhotoImage(file="images/right.png")
# checkmark = Button(image=checkmark_img, highlightthickness=0, bg="#B1DDC6", highlightbackground="#B1DDC6", command=lambda:[generate_new_word(), remove_word()])
# checkmark.grid(row=1, column=1)

# language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="#000000")
# word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="#000000")

# incorrect_img = PhotoImage(file="images/wrong.png")
# incorrect = Button(image=incorrect_img, highlightthickness=0, bg="#B1DDC6", highlightbackground="#B1DDC6", command= generate_new_word)
# incorrect.grid(row=1, column=0)

# generate_new_word()

# window.mainloop()
