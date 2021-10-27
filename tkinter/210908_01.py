from tkinter import *

class Application(Frame):
    def __init__(self, up):
        Frame.__init__(self, up)

        self.grid()

        self.chk1 = BooleanVar()
        self.chk2 = BooleanVar()
        self.chk3 = BooleanVar()

        Label(self, text='What\'s your Hobby').grid(row=0, column=0, sticky=W)

        Checkbutton(self, text='Kendo',
                    variable=self.chk1,
                    command=self.update).grid(row=1, column=0, sticky=W)
        Checkbutton(self, text='Archery',
                    variable=self.chk2,
                    command=self.update).grid(row=2, column=0, sticky=W)
        Checkbutton(self, text='Making',
                    variable=self.chk3,
                    command=self.update).grid(row=3, column=0, sticky=W)

        self.txt = Text(self, width=35, height=5, wrap=WORD)  # 리턴값 객체
        self.txt.grid(row=4, column=0, columnspan=2, sticky=W)  #

    def update(self):
        txt = ''
        if self.chk1.get():
            txt += 'You can be tanker!\n'
        if self.chk2.get():
            txt += 'You can be dealer!\n'
        if self.chk3.get():
            txt += 'You can be supporter!\n'

        self.txt.delete(0.0, END)
        self.txt.insert(0.0, txt)


app = Tk()
app.title('simple GUI 1')
app.geometry('200x180')

top = Application(app)

app.mainloop()