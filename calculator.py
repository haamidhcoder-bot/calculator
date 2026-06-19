from tkinter import *
from tkinter import messagebox
from time import sleep
import os

window=Tk()
window.title("CALCULATOR")
window.geometry("350x330")
window.maxsize(350,330)
window.config(bg="black")
window.configure()
try:
    icon_path = os.path.join(os.path.dirname(__file__), "calculator.png")
    icon = PhotoImage(file=icon_path)
    window.iconphoto(True, icon)
except:
    pass  # Icon file not found, continue without custom icon

history={}
xtra1=None

cal=Label(window,text="welcome to calculator",font=("courier new",20),bg="black",fg="white")
cal.grid()

frame1=Frame(window,bd=10,bg="black")
frame1.grid()

num=Entry(frame1,font=("courier new",15),width=15)
num.grid(row=2)

def hist():
    global xtra1
    if xtra1 is None:
        if len(history)!=0:
            xtra1=Toplevel()
            xtra1.title("history")
            xtra1.geometry("200x200")
            xtra1.config(bg="black")
            xtra1.configure()
            
            for data in history:
                L1=Label(xtra1,text=(str(data)+"="+str(history[data])),font=("courier new",12),bg="black",fg="white")
                L1.pack()

            xtra1.mainloop()
        else:
            messagebox.showwarning("no history","no calculation made")
    else:
        if xtra1.winfo_exists():
            messagebox.showwarning("Warning","close the already opened history window and check history again")
        elif not(xtra1.winfo_exists()):
            xtra1=None
            hist()



his=Button(frame1,text="i",font=("courier new",13),bg="blue",fg="white",activebackground="white",command=hist,width=1,height=1)
his.grid(row=2,column=1)

# Number pad frame
num_frame=Frame(window,bd=10,bg="black")
num_frame.grid()

def insert_num(digit):
    num.insert(END,str(digit))

def insert_decimal():
    current=num.get()
    if "." not in current:
        num.insert(END,".")

# Number buttons layout (3x3 grid + 0 + operations on the right)
# Row 0: 7, 8, 9, +
btn_7=Button(num_frame,text=" 7 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(7),font=("courier new",15),width=5)
btn_7.grid(row=0,column=0)

btn_8=Button(num_frame,text=" 8 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(8),font=("courier new",15),width=5)
btn_8.grid(row=0,column=1)

btn_9=Button(num_frame,text=" 9 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(9),font=("courier new",15),width=5)
btn_9.grid(row=0,column=2)

def add1():
    num.insert(END,"+")

add=Button(num_frame,text=" + ",bg="orange",fg="white",activebackground="white",command=add1,font=("courier new",15),width=5)
add.grid(row=0,column=3)

# Row 1: 4, 5, 6, -
btn_4=Button(num_frame,text=" 4 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(4),font=("courier new",15),width=5)
btn_4.grid(row=1,column=0)

btn_5=Button(num_frame,text=" 5 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(5),font=("courier new",15),width=5)
btn_5.grid(row=1,column=1)

btn_6=Button(num_frame,text=" 6 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(6),font=("courier new",15),width=5)
btn_6.grid(row=1,column=2)

def sub1():
    num.insert(END,"-")

sub=Button(num_frame,text=" - ",bg="orange",fg="white",activebackground="white",command=sub1,font=("courier new",15),width=5)
sub.grid(row=1,column=3)

# Row 2: 1, 2, 3, x
btn_1=Button(num_frame,text=" 1 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(1),font=("courier new",15),width=5)
btn_1.grid(row=2,column=0)

btn_2=Button(num_frame,text=" 2 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(2),font=("courier new",15),width=5)
btn_2.grid(row=2,column=1)

btn_3=Button(num_frame,text=" 3 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(3),font=("courier new",15),width=5)
btn_3.grid(row=2,column=2)

def mul1():
    num.insert(END,"x")

mul=Button(num_frame,text=" x ",bg="orange",fg="white",activebackground="white",command=mul1,font=("courier new",15),width=5)
mul.grid(row=2,column=3)

# Row 3: 0, decimal, =, ÷
btn_0=Button(num_frame,text=" 0 ",bg="gray",fg="white",activebackground="white",command=lambda:insert_num(0),font=("courier new",15),width=5)
btn_0.grid(row=3,column=0)

btn_dot=Button(num_frame,text=" . ",bg="gray",fg="white",activebackground="white",command=insert_decimal,font=("courier new",15),width=5)
btn_dot.grid(row=3,column=1)

def result():
    num1=num.get()
    value=changes(num1)
    try:
        result=eval(value)
        if value!=str(result):
            history[num1]=result
        reset()
        num.insert(0,result)
    except ZeroDivisionError:
        messagebox.showerror("ERROR","Cannot divide by zero")
        reset()
    except (ValueError, SyntaxError):
        messagebox.showerror("ERROR","Invalid calculation")
        reset()

rest=Button(num_frame,text=" = ",bg="green",fg="white",activebackground="white",command=result,font=("courier new",15),width=5)
rest.grid(row=3,column=2)

def div1():
    num.insert(END,"÷")

div=Button(num_frame,text=" ÷ ",bg="orange",fg="white",activebackground="white",command=div1,font=("courier new",15),width=5)
div.grid(row=3,column=3)

# Reset button (optional - can be placed separately or combined)
def reset():
    num.delete(0,END)

res=Button(num_frame,text="reset",bg="red",fg="white",activebackground="white",command=reset,font=("courier new",12),width=20)
res.grid(row=4,column=0,columnspan=4)

def changes(num):
    return num.replace("x", "*").replace("÷", "/")

window.mainloop()
