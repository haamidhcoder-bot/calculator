from customtkinter import *
from tkinter import messagebox,PhotoImage

window=CTk()
window.title("CALCULATOR")
window.geometry("255x255")
window.maxsize(255,255)
window.config(bg="black")
window.configure()

history={}
xtra1=None

cal=CTkLabel(window,text="welcome to calculator",font=("courier new",20),fg_color="black")
cal.grid()

frame1=CTkFrame(window)
frame1.grid()

num=CTkEntry(frame1,font=("courier new",15),width=150,height=10,corner_radius=100,fg_color="white",text_color="black")
num.grid(row=2)

def hist():
    global xtra1
    if xtra1 is None:
        if len(history)!=0:
            xtra1=CTkToplevel()
            xtra1.title("history")
            xtra1.geometry("200x200")
            xtra1.config()
            xtra1.configure()
            
            for data in history:
                L1=CTkLabel(xtra1,text=(str(data)+"="+str(history[data])),font=("courier new",12))
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



his=CTkButton(frame1,text="i",font=("courier new",13),fg_color="blue",command=hist,width=2,height=2,hover_color="red")
his.grid(row=2,column=1)

# Number pad frame
num_frame=CTkFrame(window,fg_color="black")
num_frame.grid()

def insert_num(digit):
    num.insert(END,str(digit))

def insert_decimal():
    current=num.get()
    if "." not in current:
        num.insert(END,".")

# Number buttons layout (3x3 grid + 0 + operations on the right)
# Row 0: 7, 8, 9, +
btn_7=CTkButton(num_frame,text=" 7 ",fg_color="grey",command=lambda:insert_num(7),font=("courier new",15),width=5,hover_color="red")
btn_7.grid(row=0,column=0)

btn_8=CTkButton(num_frame,text=" 8 ",fg_color="grey",command=lambda:insert_num(8),font=("courier new",15),width=5,hover_color="red")
btn_8.grid(row=0,column=1)

btn_9=CTkButton(num_frame,text=" 9 ",fg_color="grey",command=lambda:insert_num(9),font=("courier new",15),width=5,hover_color="red")
btn_9.grid(row=0,column=2)

def add1():
    num.insert(END,"+")

add=CTkButton(num_frame,text=" + ",fg_color="orange",command=add1,font=("courier new",15),width=5,hover_color="red")
add.grid(row=0,column=3)

# Row 1: 4, 5, 6, -
btn_4=CTkButton(num_frame,text=" 4 ",fg_color="grey",command=lambda:insert_num(4),font=("courier new",15),width=5,hover_color="red")
btn_4.grid(row=1,column=0)

btn_5=CTkButton(num_frame,text=" 5 ",fg_color="grey",command=lambda:insert_num(5),font=("courier new",15),width=5,hover_color="red")
btn_5.grid(row=1,column=1)

btn_6=CTkButton(num_frame,text=" 6 ",fg_color="grey",command=lambda:insert_num(6),font=("courier new",15),width=5,hover_color="red")
btn_6.grid(row=1,column=2)

def sub1():
    num.insert(END,"-")

sub=CTkButton(num_frame,text=" - ",fg_color="orange",command=sub1,font=("courier new",15),width=5,hover_color="red")
sub.grid(row=1,column=3)

# Row 2: 1, 2, 3, x
btn_1=CTkButton(num_frame,text=" 1 ",fg_color="grey",command=lambda:insert_num(1),font=("courier new",15),width=5,hover_color="red")
btn_1.grid(row=2,column=0)

btn_2=CTkButton(num_frame,text=" 2 ",fg_color="grey",command=lambda:insert_num(2),font=("courier new",15),width=5,hover_color="red")
btn_2.grid(row=2,column=1)

btn_3=CTkButton(num_frame,text=" 3 ",fg_color="grey",command=lambda:insert_num(3),font=("courier new",15),width=5,hover_color="red")
btn_3.grid(row=2,column=2)

def mul1():
    num.insert(END,"x")

mul=CTkButton(num_frame,text=" x ",fg_color="orange",command=mul1,font=("courier new",15),width=5,hover_color="red")
mul.grid(row=2,column=3)

# Row 3: 0, decimal, =, ÷
btn_0=CTkButton(num_frame,text=" 0 ",fg_color="grey",command=lambda:insert_num(0),font=("courier new",15),width=5,hover_color="red")
btn_0.grid(row=3,column=0)

btn_dot=CTkButton(num_frame,text=" . ",fg_color="grey",command=insert_decimal,font=("courier new",15),width=5,hover_color="red")
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

rest=CTkButton(num_frame,text=" = ",fg_color="green",command=result,font=("courier new",15),width=5,hover_color="red")
rest.grid(row=3,column=2)

def div1():
    num.insert(END,"÷")

div=CTkButton(num_frame,text=" ÷ ",fg_color="orange",command=div1,font=("courier new",15),width=5,hover_color="red")
div.grid(row=3,column=3)

# Reset button (optional - can be placed separately or combined)
def reset():
    num.delete(0,END)

res=CTkButton(num_frame,text="reset",fg_color="red",command=reset,font=("courier new",12),width=20,hover_color="blue")
res.grid(row=4,column=0,columnspan=4)

def changes(num):
    return num.replace("x", "*").replace("÷", "/")

window.mainloop()
