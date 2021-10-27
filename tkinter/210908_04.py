from tkinter import *

class Application(Frame):
    def __init__(self, up):
        Frame.__init__(self, up)

        self.grid()

        self.chk1 = BooleanVar()
        self.chk2 = BooleanVar()
        self.chk3 = BooleanVar()
        self.rdo1 = StringVar()
        self.rdo1.set(None)

        Label(self, text='What\'s your Hobby').grid(row=0, column=0, sticky=W)

        Label(self, text='Name').grid(row=1, column=0, sticky=W)
        self.name = Entry(self).grid(row=1, column=1, columnspan=3, sticky=W)
        Label(self, text='Age').grid(row=2, column=0, sticky=W)
        self.age = Entry(self).grid(row=2, column=1, columnspan=3, sticky=W)
        Label(self, text='Location').grid(row=3, column=0, sticky=W)
        self.location = Entry(self).grid(row=3, column=1, columnspan=3, sticky=W)

        Label(self, text='Hobby').grid(row=4, column=0, sticky=W)
        Checkbutton(self, text='Kendo',
                    variable=self.chk1).grid(row=4, column=1, sticky=E)
        Checkbutton(self, text='Archery',
                    variable=self.chk2).grid(row=4, column=2, sticky=E)
        Checkbutton(self, text='Making',
                    variable=self.chk3).grid(row=4, column=3, sticky=E)

        Label(self, text='weapon').grid(row=5, column=0, sticky=W)
        Radiobutton(self, text='Kendo',
                    variable=self.rdo1,
                    value='sword').grid(row=5, column=1, sticky=E)
        Radiobutton(self, text='Archery',
                    variable=self.rdo1,
                    value='bow').grid(row=5, column=2, sticky=E)
        Radiobutton(self, text='Making',
                    variable=self.rdo1,
                    value='hammer').grid(row=5, column=3, sticky=E)

        Button(self, text='Click to confirm',
               fg='#01F201',
               bg='#D212E2',
               command=self.update).grid(row=6, column=0, sticky=W)

        self.txt = Text(self, width=35, height=5, wrap=WORD)  # 리턴값 객체
        self.txt.grid(row=7, column=0, columnspan=2, sticky=W)  #

    def update(self):

        set = f'{self.name} + {self.age} + {self.location}'
        txt = ''
        if self.chk1.get():
            txt += 'You can be tanker!\n'
        if self.chk2.get():
            txt += 'You can be dealer!\n'
        if self.chk3.get():
            txt += 'You can be supporter!\n'
        if self.rdo1.get():
            txt += self.rdo1.get()

        self.txt.delete(0.0, END)
        self.txt.insert(0.0, txt)


app = Tk()
app.title('Homework')
app.geometry('400x300')
app['bg'] = '#000000'

top = Application(app)

app.mainloop()