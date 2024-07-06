from tkinter import * 

mygui=Tk()
mygui.geometry('500x145+250+250')
num=IntVar(mygui)
result_label=Label(mygui,text='<result will be printed here>',font=8)
result_label.grid(row=2,column=1,pady=5)

def factorial_func():
    global result_label
    result_label.destroy()
    fact = 1
    for i in range(num.get()):
        fact = fact * (i+1)

    result_label=Label(mygui,text='The factorial of ' + str(num.get()) + ' = ' + str(fact),font=20)
    result_label.grid(row=2,column=1,pady=5)



Label(mygui,text='Enter a number to get its factorial: ',font=8).grid(padx=5,row=0,column=0)
en=Entry(mygui,textvariable=num,width=25).grid(row=0,column=1)

Button(mygui,text='Calculate',command=factorial_func,width=16).grid(pady=20,row=3,column=1)



mygui.mainloop()
