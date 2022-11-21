from tkinter import *
from morse_converter import MorseConverter

# ``````````````````````````````` CONSTANT VALUE ``````````````````````````````` #

BACKGROUND_COLOR = "#0d335d"
CANVAS_COLOR = "#1a508b"
TEXT_COLOR = "#f0c929"
TEXT_FONT = ("arial", 25, "normal")

# ``````````````````````````````` FUNCTIONS ``````````````````````````````` #


def encrypt_button():
    """
    Encrypt English into MORSE CODE
    """
    message = message_cypher.get()
    result = converter.encrypt(message.upper())
    message_decypher.delete(0, END)
    return message_decypher.insert(0, result)


def decrypt_button():
    """
    Decode the MORSE CODE into English
    """
    message = message_decypher.get()
    result = converter.decrypt(message)
    message_cypher.delete(0, END)
    return message_cypher.insert(0, result)


def copy_cypher():
    """
    Copy the cypher text
    """
    text = message_cypher.get()
    return window.clipboard_append(text)


def copy_decypher():
    """
    Copy the decypher text
    """
    text = message_decypher.get()
    return window.clipboard_append(text)

# ``````````````````````````````` CLASS DECLARATION ``````````````````````````````` #


converter = MorseConverter()
window = Tk()

# ``````````````````````````````` WINDOW ``````````````````````````````` #


window.title("MORSE_CONVERTER")
window.config(padx=30, pady=30, width=500, height=250, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=480, height=230)
canvas.config(bg=CANVAS_COLOR)
canvas.grid(row=0, column=0, columnspan=2, rowspan=5)

# labels
cypher_label = Label(text="CYPHER")
cypher_label.config(bg=CANVAS_COLOR, fg=TEXT_COLOR, font=TEXT_FONT)
cypher_label.grid(row=0, column=0, columnspan=2)
decypher_label = Label(text="DECYPHER")
decypher_label.config(bg=CANVAS_COLOR, fg=TEXT_COLOR, font=TEXT_FONT)
decypher_label.grid(row=2, column=0, columnspan=2)

# entry
message_cypher = Entry(text="Enter: ENGLISH ")
message_cypher.config(width=50)
message_cypher.grid(row=1, column=0, columnspan=2)
message_decypher = Entry(text="Enter: MORSE CODE ")
message_decypher.config(width=50)
message_decypher.grid(row=3, column=0, columnspan=2)

# buttons
cypher_button = Button(text="Encrypt", command=encrypt_button)
cypher_button.grid(row=4, column=0)
decypher_button = Button(text="Decrypt", command=decrypt_button)
decypher_button.grid(row=4, column=1)
copy_cypher_button = Button(text="COPY", command=copy_cypher)
copy_cypher_button.place(x=400, y=63)
copy_decypher_button = Button(text="COPY", command=copy_decypher)

copy_decypher_button.place(x=400, y=160)
window.mainloop()
