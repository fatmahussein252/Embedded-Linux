from tkinter import * 

mygui=Tk()
mygui.geometry('400x150+250+250')
v=StringVar(mygui)

def reverse_func():
    Label(mygui,text=v.get()[::-1]).grid(row=1,column=1)

Label(mygui,text='Enter a word: ').grid(padx=10,pady=20,row=0,column=0)
Entry(mygui,textvariable=v).grid(row=0,column=1,padx=10)
Button(mygui,text='Reverse',command=reverse_func,width=16).grid(padx=10,pady=20,row=2,column=1)
    

mygui.mainloop()
