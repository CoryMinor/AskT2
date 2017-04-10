'''
Python Version: 3.6

Author: Cory Minor

Description: This program is designed as a template to help analysts as T2's a question. The input is taken from the
text fields and then added to a question string. The user then clicks copy to clipboard and a confirmation window
appears. The question is now on the users clipboard.

Copyright: 04/08/2017
'''



from tkinter import *


#function to close window via button
def close_window():
    root.destroy()

#function to copy created question to clipboard with confirmation window
def create_copy_window(question):
    window = Toplevel()

    new = Tk()
    new.withdraw()
    new.clipboard_clear()
    new.clipboard_append(question)

    window.title('Success!')
    window.focus_set()
    window.geometry('{}x{}'.format(250,100))
    window.resizable(width=False, height=False)
    window.configure(background="gray")
    copyLabel = Label(window, text="Copied to Clipboard", font=TITLE_FONT, background="gray")
    exitBut = Button(window, text="Close", bg="red", command=close_window)
    copyLabel.grid(rowspan=2, columnspan=3, row=0, column=0)
    exitBut.grid(row=2, column=1)
    window.mainloop()
    new.destroy()

#function for creating question to copy to clipboard
def create_question():
    question = "The user is a part of " + entry_1.get("1.0", 'end-1c')
    question = question + ". " + "The user is working with " + entry_2.get("1.0", 'end-1c')
    question = question + ". " + "The problem is " + entry_3.get("1.0", 'end-1c')
    question = question + ". " + "We have already done/discovered that " + entry_4.get("1.0", 'end-1c')
    question = question + ". " + "What I need from a Tier 2 is " + entry_5.get("1.0", 'end-1c') + ". "

    if checkValue.get() == 1:
        question = question + " The user is currently waiting on an answer."
    elif checkValue.get() == 0:
        question = question + " The user is not waiting on an answer."

    create_copy_window(question)

#function to traverse forwards through widgets
def forwardTab(widget):
    widget.tk_focusNext().focus_set()
    return("break")

#Function to traverse backwards through widgets
def reverseTab(widget):
    widget.tk_focusPrev().focus_set()
    return("break")

#Fonts
TITLE_FONT = ("Helvetica", 18, "bold")
QUESTION_FONT = ("Helvetica", 9, "bold")


#Creating the root obj
root = Tk()
root.geometry('{}x{}'.format(750,500))
root.resizable(width=False, height=False)
root.configure(background="gray")
root.title("How To Ask A Tier 2 A Question")

#Variables for the check button value
checkValue = IntVar()
checkValue.set(0)

#Label and entry field creation
titleLabel = Label(text="      How To Ask Tier 2 A Question", font=TITLE_FONT, background="gray")
label_1 = Label(text="What OPCO is the user in? ", font=QUESTION_FONT, background="gray")
entry_1 = Text(width = 40, height=1)
label_2 = Label(text="What application or system are you working with?", font=QUESTION_FONT, background="gray")
entry_2 = Text(width = 40, height=1)
label_3 = Label(text="What is the problem the user is having? ", font=QUESTION_FONT, background="gray")
entry_3 = Text(width = 40, height=3)
label_4 = Label(text="What have you already done or discovered through troubleshooting?", font=QUESTION_FONT, background="gray")
entry_4 = Text(width = 40, height=5)
label_5 = Label(text="What do you need from a Tier 2? ", font=QUESTION_FONT, background="gray")
entry_5 = Text(width = 40, height=5)
label_6 = Label(text="Is the user waiting for an answer?", font=QUESTION_FONT, background="gray")
check1 = Checkbutton(text="Yes", background="gray", onvalue=1, offvalue=0, variable=checkValue)

#implementation of ignoring tabs and enter for traversing
for t in (entry_1, entry_2, entry_3, entry_4, entry_5):
    t.bind('<Tab>', lambda e, t=t: forwardTab(t))
    t.bind('<Return>', lambda e, t=t: forwardTab(t))
    t.bind('<Shift-Tab>', lambda e, t=t: reverseTab(t))

#placement of widgets
titleLabel.grid(rowspan=2, columnspan=3, row=0, column=0)
label_1.grid(row=3, column=1)
label_2.grid(row=4, column=1)
label_3.grid(row=5, column=1)
label_4.grid(row=6, column=1)
label_5.grid(row=7, column=1)
label_6.grid(row=9, column=1)
entry_1.grid(row=3, column=2, pady=10)
entry_2.grid(row=4, column=2, pady=10)
entry_3.grid(row=5, column=2, pady=10)
entry_4.grid(row=6, column=2, pady=10)
entry_5.grid(row=7, column=2, pady=10)
check1.place(x=150, y=425)
button1 = Button(text="Close", bg="red", command=close_window)
button1.place(relx=1, x=-300, y=450)
button2 = Button(text="Copy To Clipboard", bg="green", command=lambda: create_question())
button2.place(relx=1, x=-200, y=450)

root.mainloop()