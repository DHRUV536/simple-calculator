global operator
operator=""
def btnclick1():
    global operator
    operator=operator +str(1)
    user_input.set(operator)
def btnclick2():
    global operator
    operator=operator +str(2)
    user_input.set(operator)
def btnclick3():
    global operator
    operator=operator +str(3)
    user_input.set(operator)
def btnclick4():
    global operator
    operator=operator +str(4)
    user_input.set(operator)
def btnclick5():
    global operator
    operator=operator +str(5)
    user_input.set(operator)
def btnclick6():
    global operator
    operator=operator +str(6)
    user_input.set(operator)
def btnclick7():
    global operator
    operator=operator +str(7)
    user_input.set(operator)
def btnclick8():
    global operator
    operator=operator +str(8)
    user_input.set(operator)
def btnclick9():
    global operator
    operator=operator +str(9)
    user_input.set(operator)
def btnclickplus():
    global operator
    operator=operator +str("+")
    user_input.set(operator)
def btnclickminus():
    global operator
    operator=operator +str("-")
    user_input.set(operator)
def btnclickmulti():
    global operator
    operator=operator +str("*")
    user_input.set(operator)
def btnclickdiv():
    global operator
    operator=operator +str("/")
    user_input.set(operator)
def btnclickeq():
    global a
    try:
       a=eval(user_input.get())
       user_input.set(a)
       global operator
       operator=""
    except:
       global label2
       label2=ttk.Label(text="INVAILID INPUT",font=('arial',15,'bold'),).grid(row=2,column=0)
       label2=ttk.Label(text="PLEAS INPUT AGAIN",font=('arial',15,'bold'),).grid(row=3,column=0)
       operator=""
def btnclick0():
    global operator
    operator=operator +str(0)
    user_input.set(operator)
def btnclickdot():
    global operator
    operator=operator +str(".")
    user_input.set(operator)
def btnclicksin():
    global operator
    operator=operator +str("sin(")
    user_input.set(operator)
def btnclickcos():
    global operator
    operator=operator +str("cos(")
    user_input.set(operator)
def btnclicktan():
    global operator
    operator=operator +str("tan(")
    user_input.set(operator)
def btnclickc():
    global operator
    operator=""
    user_input.set(operator)    
import tkinter
from tkinter import ttk
win=tkinter.Tk()
win.title("CALCULATOR")
user_input=tkinter.StringVar()
dhruv=ttk.Entry(win,font=('arial',20,'bold'),textvariable=user_input,justify='center').grid(row=1,column=0)
style=ttk.Style()
style.configure("TButton",font=('arial',15,'bold'))
label=ttk.Label(text="CALCULATOR",font=('arial',15,'italic'),).grid(row=1,column=3)
label=ttk.Label(text="DHRUV'S",font=('arial',15,'italic'),).grid(row=1,column=2)
btn1=ttk.Button(text=1,command=btnclick1).grid(row=2,column=1)
btn2=ttk.Button(text=2,command=btnclick2).grid(row=2,column=2)
btn3=ttk.Button(text=3,command=btnclick3).grid(row=2,column=3)
btn4=ttk.Button(text="+",command=btnclickplus).grid(row=2,column=4)
btn5=ttk.Button(text=4,command=btnclick4).grid(row=3,column=1)
btn6=ttk.Button(text=5,command=btnclick5).grid(row=3,column=2,)
btn7=ttk.Button(text=6,command=btnclick6).grid(row=3,column=3)
btn8=ttk.Button(text="-",command=btnclickminus).grid(row=3,column=4)
btn9=ttk.Button(text=7,command=btnclick7).grid(row=4,column=1)
btn10=ttk.Button(text=8,command=btnclick8).grid(row=4,column=2)
btn11=ttk.Button(text=9,command=btnclick9).grid(row=4,column=3)
btn12=ttk.Button(text="*",command=btnclickmulti).grid(row=4,column=4)
btn13=ttk.Button(text="/",command=btnclickdiv).grid(row=5,column=1)
btn14=ttk.Button(text="0",command=btnclick0).grid(row=5,column=2)
btn15=ttk.Button(text="=",command=btnclickeq).grid(row=5,column=3)
btn16=ttk.Button(text=".",command=btnclickdot).grid(row=5,column=4)


btn16=ttk.Button(text="C",command=btnclickc).grid(row=6,column=4)
win.mainloop()


