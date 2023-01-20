from tkinter import *

calculator = Tk()
calculator.geometry("312x515")
calculator.resizable(width=False, height=False)
calculator.title("Calculatrice")

expression = ""
input_text = StringVar()

#display input
def basic_calcul(input):
    global expression
    expression = expression + str(input)
    input_text.set(expression)

#calcul square root
def square_root():
    global expression
    expression = str(float(input_text.get()) ** 0.5)
    input_text.set(expression)

# calcul root
def root():
    global expression
    expression = str(float(input_text.get()) ** 2.0)
    input_text.set(expression)

#clear
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

#calcul result
def btn_result():
    try:
        global expression
        expression = str(eval(expression))
        input_text.set(expression)
        expression = ""
    except:
        input_text.set('ERREUR')
        expression = ""


# Frame 1 ( for the label)
labelrow = Frame(calculator)
labelrow.pack(fill="both")

# Frame 2 ( for all button)
btnrow2 = Frame(calculator)
btnrow2.pack(fill="both", expand=True, anchor=NW)

#Label
Label(labelrow, text="", textvariable=input_text, bg="white", width=41, height=6, anchor=E, padx=10).grid()

#loop create button 1 to 9
i = 1
for j in range(1, 4):
    for k in range(3):
        Button(btnrow2, command=lambda i=i: basic_calcul(i), text=i, height=5, width=10, relief=GROOVE, bg="white", bd=1).grid(row=[j], column=[k])
        calculator.bind(i, lambda event, i=i: basic_calcul(i)) #bind button 1 to 9
        i += 1


##line 1
Button(btnrow2, command=lambda: square_root(), text="SQRT", height=5, width=10, relief=GROOVE, bg="darkolivegreen1", bd=1).grid(row=0, column=0)
Button(btnrow2, command=lambda: root(), text="RT", height=5, width=10, relief=GROOVE, bg="darkolivegreen1", bd=1).grid(row=0, column=1)
Button(btnrow2, command=lambda: basic_calcul("//"), text="%", height=5, width=10, relief=GROOVE, bg="darkolivegreen1", bd=1).grid(row=0, column=2)
Button(btnrow2, command=lambda: basic_calcul("/"), text="/", height=5, width=10, relief=GROOVE, bg="darkolivegreen1", bd=1).grid(row=0, column=3)
##line 2
Button(btnrow2, command=lambda: basic_calcul("*"), text="*", height=5, width=10, relief=GROOVE, bg="darkolivegreen1", bd=1).grid(row=1, column=3)
##line 3
Button(btnrow2, command=lambda: basic_calcul("+"), text="+", height=5, width=10, relief=GROOVE, bg="darkolivegreen1", bd=1).grid(row=2, column=3)
##line 4
Button(btnrow2, command=lambda: basic_calcul("-"), text="-", height=5, width=10, relief=GROOVE, bg="darkolivegreen1", bd=1).grid(row=3, column=3)
##line 5
Button(btnrow2, command=lambda: btn_clear(), text="C", height=5, width=10, relief=GROOVE, bg="darkolivegreen3", bd=1).grid(row=4, column=0)
Button(btnrow2, command=lambda: basic_calcul("."), text=".", height=5, width=10, relief=GROOVE, bg="darkolivegreen1", bd=1).grid(row=4, column=1)
Button(btnrow2, command=lambda: basic_calcul(0), text="0", height=5, width=10, relief=GROOVE, bg="white", bd=1).grid(row=4, column=2)
calculator.bind(0, lambda event: basic_calcul(0))
Button(btnrow2, command=lambda: btn_result(), text="=", height=5, width=10, relief=GROOVE, bg="darkolivegreen3", bd=1).grid(row=4, column=3)


calculator.mainloop()
