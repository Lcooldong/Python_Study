from tkinter import *

app = Tk()
app.title('simple GUI 1')
app.geometry('200x100')

top = Frame(app)
top.grid()

lbl = Label(top, text='Label1')
lbl.grid()

btn1 = Button(top, text='Button1')
btn1.grid()

btn2 = Button(top)
btn2.grid()
btn2.configure(text='Button2')

btn3 = Button(top)
btn3.grid()
btn3['text'] = 'Button3'

app.mainloop()


