from tkinter import *

root = Tk()

root.title("Calculator")    # Set window title
root.resizable(False, False)    # Make window unresizable

# Entry
screen_num = StringVar()
entry = Entry(root, font="Menlo 18", width=24, textvariable=screen_num)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Functions

def write(value):
    entry["state"] = NORMAL
    if len(entry.get()) == 0 and value == '0':
        pass
    elif len(entry.get()) == 0 and value == '.':
        screen_num.set('0.')
    else: 
        screen_num.set(entry.get() + value)
    entry["state"] = DISABLED

def delete():
    entry["state"] = NORMAL
    entry.delete(0, END)
    entry["state"] = DISABLED

def delete_char():
    entry["state"] = NORMAL
    screen_num.set((entry.get())[:-1])
    entry["state"] = DISABLED

def toggle_symbol():
    entry["state"] = NORMAL
    if (entry.get()).startswith("-"):
        entry.delete(0, 1)
    else:
        entry.insert(0, "-")
    entry["state"] = DISABLED

def percent():
    entry["state"] = NORMAL
    screen_num.set(eval(entry.get() + "/100"))
    entry["state"] = DISABLED

def add():
    global n1, operation
    entry["state"] = NORMAL
    n1 = entry.get()
    entry.delete(0, END)
    operation = "add"
    entry["state"] = DISABLED

def subtract():
    global n1, operation
    entry["state"] = NORMAL
    n1 = entry.get()
    entry.delete(0, END)
    operation = "subtract"
    entry["state"] = DISABLED

def mult():
    global n1, operation
    entry["state"] = NORMAL
    n1 = entry.get()
    entry.delete(0, END)
    operation = "mult"
    entry["state"] = DISABLED

def div():
    global n1, operation
    entry["state"] = NORMAL
    n1 = entry.get()
    entry.delete(0, END)
    operation = "div"
    entry["state"] = DISABLED

def get_result():
    global n1, n2, operation
    entry["state"] = NORMAL
    n2= entry.get()
    if operation == "add":
        screen_num.set(eval(f"{n1} + {n2}"))
    elif operation == "subtract":
        screen_num.set(eval(f"{n1} - {n2}"))
    elif operation == "mult":
        screen_num.set(eval(f"{n1} * {n2}"))
    elif operation == "div": 
        screen_num.set(eval(f"{n1} / {n2}"))
    entry["state"] = DISABLED

# Keybindings
root.bind("<Return>", lambda x: get_result())
root.bind("</>", lambda x: div())
root.bind("<*>", lambda x: mult())
root.bind("<+>", lambda x: add())
root.bind("<minus>", lambda x: subtract())

root.bind("<Key-1>", lambda x: write("1"))
root.bind("<Key-2>", lambda x: write("2"))
root.bind("<Key-3>", lambda x: write("3"))
root.bind("<Key-4>", lambda x: write("4"))
root.bind("<Key-5>", lambda x: write("5"))
root.bind("<Key-6>", lambda x: write("6"))
root.bind("<Key-7>", lambda x: write("7"))
root.bind("<Key-8>", lambda x: write("8"))
root.bind("<Key-9>", lambda x: write("9"))
root.bind("<Key-0>", lambda x: write("0"))
root.bind("<.>", lambda x: write("."))

root.bind("<BackSpace>", lambda x: delete_char())
root.bind("<Delete>", lambda x: delete())
root.bind("<%>", lambda x: percent())
root.bind("<Control-minus>", lambda x: toggle_symbol())

# Buttons
button_1 = Button(root, text="1", width=3, height=2, command=lambda: write("1"))
button_2 = Button(root, text="2", width=3, height=2, command=lambda: write("2"))
button_3 = Button(root, text="3", width=3, height=2, command=lambda: write("3"))
button_4 = Button(root, text="4", width=3, height=2, command=lambda: write("4"))
button_5 = Button(root, text="5", width=3, height=2, command=lambda: write("5"))
button_6 = Button(root, text="6", width=3, height=2, command=lambda: write("6"))
button_7 = Button(root, text="7", width=3, height=2, command=lambda: write("7"))
button_8 = Button(root, text="8", width=3, height=2, command=lambda: write("8"))
button_9 = Button(root, text="9", width=3, height=2, command=lambda: write("9"))
button_0 = Button(root, text="0", width=12, height=2, command=lambda: write("0"))

button_del = Button(root, text="AC", width=3, height=2, command=delete)
button_plusminus = Button(root, text="±", width=3, height=2, command=toggle_symbol) 
button_percent = Button(root, text="%", width=3, height=2, command=percent)
button_div = Button(root, text="÷", width=3, height=2, command=div)
button_mult= Button(root, text="×", width=3, height=2, command=mult)
button_minus = Button(root, text="-", width=3, height=2, command=subtract)
button_plus = Button(root, text="+", width=3, height=2, command=add)
button_point = Button(root, text=".", width=3, height=2, command=lambda: write("."))
button_equals = Button(root, text="=", width=3, height=2, command=get_result)

# Placing buttons inside our GUI
# Row 1
button_del.grid(row=1, column=0)
button_plusminus.grid(row=1, column=1)
button_percent.grid(row=1, column=2)
button_div.grid(row=1, column=3)

# Row 2
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mult.grid(row=2, column=3)

# Row 3
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_minus.grid(row=3, column=3)

# Row 4
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_plus.grid(row=4, column=3)

# Row 5
button_0.grid(row=5, column=0, columnspan=2)
button_point.grid(row=5, column=2)
button_equals.grid(row=5, column=3)

# Disable entry
entry.config(disabledbackground="#EDECED" , disabledforeground="black", highlightthickness=2, state=DISABLED)

root.mainloop()
