import tkinter
from tkinter import*
root=Tk()
root.title("Calculator")
root.geometry("250x300")
root.resizable(False,False)
root.config(bg="gray")
label_result=Label(root,width=70,height=3,font=("Aerial",12),text="")
label_result.pack()
def clear():
    global equation
    equation=""
    label_result.config(text=equation)
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="Syntax error"
            equation=""
    label_result.config(text=result)

Button(root,width=5,height=1,text="C",font=("Aerial",12,"bold"),bd=1,fg="white",bg="black",command=lambda:clear()).place(x=10,y=70)
Button(root,width=5,height=1,text="1",font=("Aerial",12,"bold"),bd=1,fg="white",bg="black",command=lambda:show("1")).place(x=70,y=70)
Button(root,width=5,height=1,text="2",font=("Aerial",12,"bold"),bd=1,fg="white",bg="black",command=lambda:show("2")).place(x=130,y=70)
Button(root,width=5,height=1,text="3",font=("Aerial",12,"bold"),bd=1,fg="white",bg="black",command=lambda:show("3")).place(x=190,y=70)

Button(root,width=5,height=1,text="4",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("4")).place(x=10,y=110)
Button(root,width=5,height=1,text="5",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("5")).place(x=70,y=110)
Button(root,width=5,height=1,text="6",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("6")).place(x=130,y=110)
Button(root,width=5,height=1,text="7",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("7")).place(x=190,y=110)

Button(root,width=5,height=1,text="8",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("8")).place(x=10,y=150)
Button(root,width=5,height=1,text="9",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("9")).place(x=70,y=150)
Button(root,width=5,height=1,text="0",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("0")).place(x=130,y=150)
Button(root,width=5,height=1,text=".",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show(".")).place(x=190,y=150)

Button(root,width=5,height=1,text="+",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("+")).place(x=10,y=190)
Button(root,width=5,height=1,text="-",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("-")).place(x=70,y=190)
Button(root,width=5,height=1,text="/",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("/")).place(x=130,y=190)
Button(root,width=5,height=1,text="*",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("*")).place(x=190,y=190)

Button(root,width=5,height=3,text="(",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("(")).place(x=10,y=230)
Button(root,width=5,height=3,text=")",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show(")")).place(x=70,y=230)
Button(root,width=5,height=3,text="%",font=("Aerial",12,"bold"),bd=1,fg="black",bg="blue",command=lambda:show("%")).place(x=130,y=230)
Button(root,width=5,height=3,text="=",font=("Aerial",12,"bold"),bd=1,fg="black",bg="gold",command=lambda:calculate()).place(x=190,y=230)




root=mainloop()