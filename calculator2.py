from tkinter import*
from tkinter import messagebox
import math
window=Tk()
window.maxsize(width='400',height='430')
window.minsize(width='400',height='430')
window.title("Calculator")
window.configure(bg='steelblue')
window.iconbitmap('Iconleak-Atrous-Calculator.ico')

text= StringVar()
operator=''

def click(number):
    global operator
    operator +=str(number)
    text.set(operator)

def clear():
    global operator
    operator = ''
    text.set(operator)

def equal():
    try:
        global operator
        result= eval(operator)
        operator=str(result)
        text.set(result)

    except:
        messagebox.showinfo('Alert','Somthing is wrong \n please try again')

def cmsin():
    try:
        global operator
        result=math.sin(eval(text.get()))
        operator=str(result)
        text.set(result)
    except:
        messagebox.showinfo('Alert','Somthing is wrong \n please try again')   


def cmcos():
    try:
        global operator
        result=math.cos(eval(text.get()))
        operator=str(result)
        text.set(result)
    except:
        messagebox.showinfo('Alert','Somthing is wrong \n please try again')

def cmtan():
    try:
        global operator
        result=math.tan(eval(text.get()))
        operator=str(result)
        text.set(result)
    except:
        messagebox.showinfo('Alert','Somthing is wrong \n please try again')
        


def cmlog():
    try:
        global operator
        result=math.log(eval(text.get()))
        operator=str(result)
        text.set(result)
    except:
        messagebox.showinfo('Alert','Somthing is wrong \n please try again')        


def cmsqrt():
    try:
        global operator
        result=math.sqrt(eval(text.get()))
        operator=str(result)
        text.set(result)
    except:
        messagebox.showinfo('Alert','Somthing is wrong \n please try again')        

   
#*********************************************************bind function****************************************************************

def on_enter7(e):
     btn7.configure(bg='white',fg='blue')

def on_leave7(e):
    btn7.configure(bg='powderblue',fg='black')


def on_enter8(e):
     btn8.configure(bg='white',fg='blue')

def on_leave8(e):
    btn8.configure(bg='powderblue',fg='black')
        
def on_enter9(e):
     btn9.configure(bg='white',fg='blue')

def on_leave9(e):
    btn9.configure(bg='powderblue',fg='black')

def on_enterplus(e):
     btnplus.configure(bg='white',fg='blue')

def on_leaveplus(e):
    btnplus.configure(bg='powderblue',fg='black')
        
def on_enter4(e):
     btn4.configure(bg='white',fg='blue')

def on_leave4(e):
    btn4.configure(bg='powderblue',fg='black')

def on_enter5(e):
     btn5.configure(bg='white',fg='blue')

def on_leave5(e):
    btn5.configure(bg='powderblue',fg='black')

def on_enter6(e):
     btn6.configure(bg='white',fg='blue')

def on_leave6(e):
    btn6.configure(bg='powderblue',fg='black')

def on_enterminus(e):
     btnminus.configure(bg='white',fg='blue')

def on_leaveminus(e):
    btnminus.configure(bg='powderblue',fg='black')
        
def on_enter1(e):
     btn1.configure(bg='white',fg='blue')

def on_leave1(e):
    btn1.configure(bg='powderblue',fg='black')
                
def on_enter2(e):
     btn2.configure(bg='white',fg='blue')

def on_leave2(e):
    btn2.configure(bg='powderblue',fg='black')

def on_enter3(e):
     btn3.configure(bg='white',fg='blue')

def on_leave3(e):
    btn3.configure(bg='powderblue',fg='black')
        
def on_entermult(e):
     btnmult.configure(bg='white',fg='blue')

def on_leavemult(e):
    btnmult.configure(bg='powderblue',fg='black')

def on_enterequal(e):
     btnequal.configure(bg='white',fg='blue')

def on_leaveequal(e):
    btnequal.configure(bg='powderblue',fg='black')

def on_enterc(e):
     btnc.configure(bg='white',fg='blue')

def on_leavec(e):
    btnc.configure(bg='powderblue',fg='black')
        
def on_enterzero(e):
     btnzero.configure(bg='white',fg='blue')

def on_leavezero(e):
    btnzero.configure(bg='powderblue',fg='black')
            
def on_enterdiv(e):
     btndiv.configure(bg='white',fg='blue')

def on_leavediv(e):
    btndiv.configure(bg='powderblue',fg='black')

def on_entertext(e):
    entry.configure(bg='white',fg='blue')
def on_leavetext(e):
    entry.configure(bg='powderblue',fg='black')


def on_entersin(e):
    btnsin.configure(bg='white',fg='blue')
def on_leavesin(e):
    btnsin.configure(bg='powderblue',fg='black')

def on_entercos(e):
    btncos.configure(bg='white',fg='blue')
def on_leavecos(e):
    btncos.configure(bg='powderblue',fg='black')
    
def on_entertan(e):
    btntan.configure(bg='white',fg='blue')
def on_leavetan(e):
    btntan.configure(bg='powderblue',fg='black')

def on_enterlog(e):
    btnlog.configure(bg='white',fg='blue')
def on_leavelog(e):
    btnlog.configure(bg='powderblue',fg='black')

def on_entersqrt(e):
    btnsqrt.configure(bg='white',fg='blue')
def on_leavesqrt(e):
    btnsqrt.configure(bg='powderblue',fg='black')   
                    
#*****************************************************Button***********************************************************************************************************
entry=Entry(window,bg="powderblue",font=('arial',20,'italic bold'),bd=5,justify="right",textvariable=text)
entry.grid(row=0,columnspan=4)

entry.bind('<Enter>',on_entertext)
entry.bind('<Leave>',on_leavetext)

btn7=Button(window,text="7",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(7),activebackground='blue',activeforeground='white')
btn7.grid(row=1,column=0)

btn8=Button(window,text="8",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3 ,command=lambda:click(8),activebackground='blue',activeforeground='white')
btn8.grid(row=1,column=1)

btn9=Button(window,text="9",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(9),activebackground='blue',activeforeground='white')
btn9.grid(row=1,column=2)

btnplus=Button(window,text="+",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click('+'),activebackground='blue',activeforeground='white')
btnplus.grid(row=1,column=3)

btn4=Button(window,text="4",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(4),activebackground='blue',activeforeground='white')
btn4.grid(row=2,column=0)

btn5=Button(window,text="5",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(5),activebackground='blue',activeforeground='white')
btn5.grid(row=2,column=1)

btn6=Button(window,text="6",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(6),activebackground='blue',activeforeground='white')
btn6.grid(row=2,column=2)

btnminus=Button(window,text=" -",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click('-'),activebackground='blue',activeforeground='white')
btnminus.grid(row=2,column=3)

btn1=Button(window,text="1",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(1),activebackground='blue',activeforeground='white')
btn1.grid(row=3,column=0)

btn2=Button(window,text="2",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(2),activebackground='blue',activeforeground='white')
btn2.grid(row=3,column=1)

btn3=Button(window,text="3",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(3),activebackground='blue',activeforeground='white')
btn3.grid(row=3,column=2)

btnmult=Button(window,text=" *",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click('*'),activebackground='blue',activeforeground='white')
btnmult.grid(row=3,column=3)



btnequal=Button(window,text=" =",font=('arial',20,'bold'),bg='powderblue',padx='12',pady='15',bd=3, command=equal,activebackground='blue',activeforeground='white')
btnequal.grid(row=4,column=3)

btnc=Button(window,text="c",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=clear,activebackground='blue',activeforeground='white')
btnc.grid(row=4,column=0)

btnzero=Button(window,text="0",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click(0),activebackground='blue',activeforeground='white')
btnzero.grid(row=4,column=1)

btndiv=Button(window,text=" /",font=('arial',20,'bold'),bg='powderblue',padx='15',pady='15',bd=3,command=lambda:click('/'),activebackground='blue',activeforeground='white')
btndiv.grid(row=4,column=2)


#****************************************************************************************************************************************************************************

btnsin=Button(window,text=" sin",font=('arial',20,'bold'),bg='powderblue',padx='5',pady='15',bd=3,command=cmsin,activebackground='blue',activeforeground='white')
btnsin.grid(row=0,column=4)


btncos=Button(window,text="cos",font=('arial',20,'bold'),bg='powderblue',padx='5',pady='15',bd=3,command= cmcos,activebackground='blue',activeforeground='white')
btncos.grid(row=1,column=4)

btntan=Button(window,text=" tan",font=('arial',20,'bold'),bg='powderblue',padx='5',pady='15',bd=3,command= cmtan,activebackground='blue',activeforeground='white')
btntan.grid(row=2,column=4)

btnlog=Button(window,text=" log",font=('arial',20,'bold'),bg='powderblue',padx='5',pady='15',bd=3,command= cmlog,activebackground='blue',activeforeground='white')
btnlog.grid(row=3,column=4)

btnsqrt=Button(window,text="sqrt",font=('arial',20,'bold'),bg='powderblue',padx='5',pady='15',bd=3,command= cmsqrt,activebackground='blue',activeforeground='white')
btnsqrt.grid(row=4,column=4)

 

#************************************************************** binding *********************************************************************************************************

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnplus.bind('<Enter>',on_enterplus)
btnplus.bind('<Leave>',on_leaveplus)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnminus.bind('<Enter>',on_enterminus)
btnminus.bind('<Leave>',on_leaveminus)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btnmult.bind('<Enter>',on_entermult)
btnmult.bind('<Leave>',on_leavemult)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btnc.bind('<Enter>',on_enterc)
btnc.bind('<Leave>',on_leavec)

btnzero.bind('<Enter>',on_enterzero)
btnzero.bind('<Leave>',on_leavezero)

btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

window.mainloop()
