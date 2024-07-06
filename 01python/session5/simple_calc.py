from tkinter import * 

mygui=Tk()
mygui.geometry('400x200+250+250')
num1=IntVar(mygui)
num2=IntVar(mygui)
b1=StringVar(mygui)
result_label=Label(mygui,text='<result will be printed here>')
result_label.grid(row=2,column=1,pady=5)

def calc_func():
    global result_label
    result_label.destroy()
    if b1.get() == 'Sum':
     result = num1.get() + num2.get()
     result_label=Label(mygui,text='The Sum is: '+ str(num1.get()) + '+' + str(num2.get() )+ '=' + str(result))
     result_label.grid(row=2,column=1,pady=5)
    elif b1.get() == 'Sub':
     result = num1.get() - num2.get()
     result_label=Label(mygui,text='The Sub is: '+ str(num1.get()) + '+' + str(num2.get() )+ '=' + str(result))
     result_label.grid(row=2,column=1,pady=5)
    else:
      result_label=Label(mygui,text='No checked operation')
      result_label.grid(row=2,column=1,pady=5)

lb1=Label(mygui,text='Enter the value of M: ').grid(padx=5,row=0,column=0)
en1=Entry(mygui,textvariable=num1).grid(row=0,column=1)

lb2=Label(mygui,text='Enter the value of N: ').grid(padx=5,row=1,column=0)
en2=Entry(mygui,textvariable=num2).grid(row=1,column=1)

Button(mygui,text='Calculate',command=calc_func,width=16).grid(pady=20,row=3,column=1)

Radiobutton(mygui,text='Sum',variable=b1,value='Sum',width=10,activeforeground='purple',anchor='sw',tristatevalue=1).grid(row=4,column=0)
Radiobutton(mygui,text='Sub',variable=b1,value='Sub',width=10,activeforeground='purple',anchor='sw',tristatevalue=1).grid(row=5,column=0)

mygui.mainloop()
