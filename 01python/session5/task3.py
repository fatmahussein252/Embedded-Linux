from tkinter import * 

mygui=Tk()
mygui.geometry('400x180+250+250')
num1=IntVar(mygui)
num2=IntVar(mygui)
b1=StringVar(mygui)


def calc_func():
    if b1.get() == 'Sum':
     result = num1.get() + num2.get()
     Label(mygui,text='The Sum is: '+ str(num1.get()) + '+' + str(num2.get() )+ '=' + result).grid(row=2,column=1)
    else:
     result = num1.get() - num2.get()
     Label(mygui,text='The Sub is: '+ str(num1.get()) + '+' + str(num2.get() )+ '=' + result).grid(row=2,column=1)

lb1=Label(mygui,text='Enter the value of M: ').grid(padx=10,row=0,column=0)
en1=Entry(mygui,textvariable=num1).grid(row=0,column=1,padx=10)

lb2=Label(mygui,text='Enter the value of N: ').grid(padx=10,row=1,column=0)
en2=Entry(mygui,textvariable=num2).grid(row=1,column=1,padx=10)
Button(mygui,text='Calculate',command=calc_func,width=16).grid(padx=10,pady=20,row=3,column=1)

Radiobutton(mygui,text='Sum',variable=b1).grid(padx=5)
Radiobutton(mygui,text='Sub',variable=b1).grid(padx=5)

mygui.mainloop()
