from tkinter import *

mygui=Tk()
mygui.title('Buttons')
mygui.geometry('160x80+100+100')
Button(mygui,text='Button1').grid(row=1,column=2)
Button(mygui,text='Button2').grid(row=2,column=1)
Button(mygui,text='Button3').grid(row=3,column=2)
Button(mygui,text='Button4').grid(row=2,column=3)
mygui.mainloop()
