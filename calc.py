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
    if (entry.get()).startswith("0"):
        screen_num.set((entry.get())[:-1])
    screen_num.set(entry.get() + value)

def delete():
    entry.delete(0, END)

def toggle_symbol():
    if (entry.get()).startswith("-"):
        entry.delete(0, 1)
    else:
        entry.insert(0, "-")

def percent():
    screen_num.set(eval(entry.get() + "/100"))

def add():
    global n1, operation
    n1 = entry.get()
    entry.delete(0, END)
    operation = "add"

def subtract():
    global n1, operation
    n1 = entry.get()
    entry.delete(0, END)
    operation = "subtract"

def mult():
    global n1, operation
    n1 = entry.get()
    entry.delete(0, END)
    operation = "mult"

def div():
    global n1, operation
    n1 = entry.get()
    entry.delete(0, END)
    operation = "div"

def get_result():
    global n1, n2, operation
    n2= entry.get()
    if operation == "add":
        screen_num.set(eval(f"{n1} + {n2}"))
    elif operation == "subtract":
        screen_num.set(eval(f"{n1} - {n2}"))
    elif operation == "mult":
        screen_num.set(eval(f"{n1} * {n2}"))
    elif operation == "div": 
        screen_num.set(eval(f"{n1} / {n2}"))

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

root.mainloop()
