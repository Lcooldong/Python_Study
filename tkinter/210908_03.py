from tkinter import *


class Application(Frame):
    def __init__(self, up):
        Frame.__init__(self, up)

        self.grid()

        self.rdo1 = StringVar()
        self.rdo1.set(None)

        Label(self, text='What\'s your Hobby').grid(row=0, column=0, sticky=W)

        Radiobutton(self, text='Kendo',
                    variable=self.rdo1,
                    value='sword',
                    command=self.update).grid(row=1, column=0, sticky=W)
        Radiobutton(self, text='Archery',
                    variable=self.rdo1,
                    value='bow',
                    command=self.update).grid(row=2, column=0, sticky=W)
        Radiobutton(self, text='Making',
                    variable=self.rdo1,
                    value='hammer',
                    command=self.update).grid(row=3, column=0, sticky=W)

        self.txt = Text(self, width=35, height=5, wrap=WORD)  # 리턴값 객체
        self.txt.grid(row=4, column=0, columnspan=2, sticky=W)  # 위치

    def update(self):
        # txt = ''
        # if self.rdo1.get():
        #     txt += self.rdo1.get()
        txt = f'My tools : {self.rdo1.get()}'

        self.txt.delete(0.0, END)
        self.txt.insert(0.0, txt)


app = Tk()
app.title('T')
app.geometry('200x180')

top = Application(app)

app.mainloop()