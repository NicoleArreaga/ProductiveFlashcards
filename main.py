from tkinter import *   #tkinter has been a great mode for us to use while weve been creating our productivity stuff
from random import randint

root = Tk()
root.title('Spanish Flashcards')    #decided to focus on Spanish since Julia and I have an exam for Spanish
root.geometry("550x410")

words = [
    (("Poner"), ("To wear")),           # I chose these words because these are verbs that are the most common and important in Spanish
    (("Aprender"), ("To learn")),
    (("Tener"), ("To have")),
    (("Hacer"), ("To do")),
    (("Saber"), ("To know")),
    (("Poder"), ("To be able to")),
    (("Decir"), ("To say")),
    (("Jugar"), ("To play")),
    (("Hablar"), ("To talk")),
    (("Mirar"), ("To watch")),
    (("Escribir"), ("To write")),
    (("Pensar"), ("To think")),
    (("Venir"), ("To come")),
    (("Traer"), ("To bring")),
    (("Querer"), ("To want")),
    (("Ayudar"), ("To help")),
    (("Levantar"), ("To get up")),
    (("Banar"), ("To bathe")),
    (("Escuchar"), ("To listen")),
    (("Tomar"), ("To drink"))
]

# get a count of the word list
count = len(words)


def next():
    global hinter, hint_count
    # Clear the screen
    answer_label.config(text="")
    my_entry.delete(0, END)     # this is used because then "incorrect/correct" or our answer will not appear for the next word
    hint_label.config(text="")
    # Reset Hint stuff
    hinter = ""
    hint_count = 0

    # Create random selection
    global random_word
    random_word = randint(0, count-1)
    # update label with Spanish Words
    spanish_word.config(text=words[random_word][0])


def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")      # purpose is for telling if u are correct or incorrect
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")    # purpose is for telling if u are correct or incorrect


# Keep track of the hints
hinter = ""
hint_count = 0


def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count += 1


# Labels
spanish_word = Label(root, text="", font=("Times New Roman", 36))  # font style and size
spanish_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry = Entry(root, font=("Times New Roman", 18))  # font style and size
my_entry.pack(pady=20)

# Create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)    #to separate each button from each other

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=1,)

hint_button = Button(button_frame, text="Hint", command=hint)   #hint button is included because it is very important and is a great help
hint_button.grid(row=0, column=2, padx=20)

# Create hint label
hint_label = Label(root, text="")
hint_label.pack(pady=20)

# Run next function when program starts
next()

root.mainloop()
