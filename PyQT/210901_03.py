from tkinter import *


class Application(Frame):
    def __init__(self, up):
        Frame.__init__(self, up)
        self.grid()

        lbl = Label(self, text='Label1')
        lbl.grid()

        btn1 = Button(self, text='Button1')
        btn1.grid()

        btn2 = Button(self)
        btn2.grid()
        btn2.configure(text='Button2')

        btn3 = Button(self)
        btn3.grid()
        btn3['text'] = 'Button3'


app = Tk()
app.title('simple GUI 1')
app.geometry('200x100')

top = Application(app)

app.mainloop()


