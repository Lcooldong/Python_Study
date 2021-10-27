from tkinter import *


class Application(Frame):
    def __init__(self, up):
        Frame.__init__(self, up)
        self.grid()

        self.lbl1 = Label(self, text='패스워드를 입력하세요')
        self.lbl1.grid(row=0, column=0, columnspan=2, sticky=W)    # 열방향 2개

        self.lbl2 = Label(self, text='패스워드: ')
        self.lbl2.grid(row=1, column=0, sticky=W)

        self.pwd = Entry(self)
        self.pwd.grid(row=1, column=1, sticky=W)

        self.btn1 = Button(self, text='확인', command=self.update)
        self.btn1.grid(row=2, column=0, sticky=W)

        self.msg = Text(self, width=35, height=5, wrap=WORD)
        self.msg.grid(row=3, column=0, columnspan=2, sticky=W)

    def update(self):
        pwd = self.pwd.get()
        if pwd == '123':
            txt = '맞습니다.'
        else:
            txt = '틀렸습니다.'

        self.msg.delete(0.0, END)
        self.msg.insert(0.0, txt)


app = Tk()
app.title('simple GUI 1')
app.geometry('200x100')

top = Application(app)

app.mainloop()