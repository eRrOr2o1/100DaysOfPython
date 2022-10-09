from tkinter import *

# import * ---> imports every single class


window = Tk()  # Create a blank screen
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am A Label", font=("Arial", 24, "bold"))
my_label.pack()  # Used to load out label in the screen

# Add or Update new text using 2 ways
# Way 1
# my_label["text"] = "New Text"
# Way 2
my_label.config(text="New Text")

# Entry

input = Entry(width=30)
# Add some text to begin with
input.insert(END, string="Some text to begin with")
# Gets text in entry
input.get()
input.pack()

# Textbox
text = Text(height=5, width=30)
# Put cursor in textbox
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Button

def button_clicked():
    input_text = input.get()
    my_label.config(text=input_text)
    # print("I got clicked")


button = Button(text="Click Me",
                command=button_clicked)  # Command sets the function so that by clicking button it works
button.pack()

window.mainloop()  # Keep the window on screen
