from tkinter import *
import tkinter.font as tkFont

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("HOME")
        self.pack(fill=X)

        subjectFont = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
        font1 = tkFont.Font(family="Arial", size=12, weight="bold", slant="italic")
        font2 = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")
        entryFont = tkFont.Font(family="Arial", size=10, weight="bold", slant="italic")
        txtFont = tkFont.Font(family="Arial", size=14, weight="bold", slant="italic")

        self.leftFrame = Frame(self, bg='black')
        self.leftFrame.pack(fill=BOTH, ipadx=40, ipady=200, side=LEFT)

        self.topLabel = Label(self.leftFrame)
        self.topLabel.pack(fill=X, side=TOP, ipady=40)

        lbl1 = Label(self.leftFrame, text='Name', width=20, height=2, bg='purple')
        lbl1.pack(fill=X, side=TOP)
        lbl1.configure(font=font1)

        lbl2 = Label(self.leftFrame, text='Age', width=20, height=2, bg='skyBlue')
        lbl2.pack(fill=X, side=TOP)
        lbl2.configure(font=font1)
        lbl3 = Label(self.leftFrame, text='Gender', width=20, height=2, bg='magenta')
        lbl3.pack(fill=X, side=TOP)
        lbl3.configure(font=font1)
        lbl4 = Label(self.leftFrame, text='Location', width=20, height=2, bg='brown')
        lbl4.pack(fill=X, side=TOP)
        lbl4.configure(font=font1)
        lbl5 = Label(self.leftFrame, text='Hobby', width=20, height=2, bg='cyan')
        lbl5.pack(fill=X, side=TOP)
        lbl5.configure(font=font1)

        self.frame1 = Frame(self, bg='red')
        self.frame1.pack(fill=X, ipady=5)
        self.frame2 = Frame(self, bg='orange')
        self.frame2.pack(fill=BOTH, ipady=7)
        self.frame3 = Frame(self, bg='yellow')
        self.frame3.pack(fill=BOTH, ipady=7)
        self.frame4 = Frame(self, bg='green')
        self.frame4.pack(fill=BOTH, ipady=7)
        self.frame5 = Frame(self, bg='blue')
        self.frame5.pack(fill=BOTH, ipady=7)
        self.frame6 = Frame(self, bg='darkBlue')
        self.frame6.pack(fill=BOTH, ipady=8)
        self.frame7 = Frame(self, bg='purple')
        self.frame7.pack(fill=BOTH, ipady=10)
        self.frame8 = Frame(self)
        self.frame8.pack(fill=BOTH, ipady=10)

        lblSubject = Label(self.frame1, text='Membership Cofiguration', width=20, height=2, bg='firebrick4')
        lblSubject.pack(fill=BOTH, padx=20, pady=18)
        lblSubject.configure(font=subjectFont)

        self.entryName = Entry(self.frame2, width=30, font=entryFont)
        self.entryName.pack(side=LEFT, padx=10, ipady=5)
        self.entryAge = Entry(self.frame3, width=10, font=entryFont)
        self.entryAge.pack(side=LEFT, padx=10, ipady=5)
        self.entryLocale = Entry(self.frame5, width=80, font=entryFont)
        self.entryLocale.pack(side=LEFT, padx=10, ipady=5)

        self.rdo1 = StringVar()
        self.rdo1.set(None)

        self.r1 = Radiobutton(self.frame4, text='Male', font=font2, variable=self.rdo1, value='Male')
        self.r1.pack(side=LEFT, padx=20)
        self.r2 = Radiobutton(self.frame4, text='Female', font=font2, variable=self.rdo1, value='Female')
        self.r2.pack(side=LEFT, padx=20)
        self.r3 = Radiobutton(self.frame4, text='Bi', font=font2, variable=self.rdo1, value='Bi')
        self.r3.pack(side=LEFT, padx=20)

        self.chk1 = BooleanVar()
        self.chk2 = BooleanVar()
        self.chk3 = BooleanVar()
        self.chk4 = BooleanVar()

        self.checkBtn1 = Checkbutton(self.frame6, text='Kendo', font=font2, variable=self.chk1)
        self.checkBtn1.pack(side=LEFT, padx=20)
        self.checkBtn2 = Checkbutton(self.frame6, text='Archery', font=font2, variable=self.chk2)
        self.checkBtn2.pack(side=LEFT, padx=20)
        self.checkBtn3 = Checkbutton(self.frame6, text='Making', font=font2, variable=self.chk3)
        self.checkBtn3.pack(side=LEFT, padx=20)
        self.checkBtn4 = Checkbutton(self.frame6, text='drawing', font=font2, variable=self.chk4)
        self.checkBtn4.pack(side=LEFT, padx=20)

        self.confirmBtn = Button(self.frame7, text='Confirm', fg='#01F201', bg='#D212E2', command=self.update)
        self.confirmBtn.pack(side=LEFT, padx=50, ipadx=4, ipady=5)

        self.eraseBtn = Button(self.frame7, text='ERASE', fg='#01F201', bg='#D212E2', command=self.erase)
        self.eraseBtn.pack(side=RIGHT, padx=50, ipadx=8, ipady=5)

        self.txt = Text(self.frame8, width=35, height=5, wrap=WORD, font=txtFont)  # 리턴값 객체
        self.txt.pack(fill=BOTH, side=TOP, ipady=50)

        self.buttomFrame = Frame(self, bg='purple')
        self.buttomFrame.pack(fill=Y)

    def update(self):
        txt = f'Name : {self.entryName.get()}\n' + \
              f'Age : {self.entryAge.get()}\n' + \
              f'Location : {self.entryLocale.get()}\n'
        if self.rdo1.get():
            txt += 'Gender : ' + self.rdo1.get() + '\n'
        if self.chk1.get():
            txt += 'You can be tanker!\n'
        if self.chk2.get():
            txt += 'You can be dealer!\n'
        if self.chk3.get():
            txt += 'You can be supporter!\n'
        if self.chk4.get():
            txt += 'You can be artist!\n'

        self.txt.delete(0.0, END)
        self.txt.insert(0.0, txt)

    def erase(self):
        self.txt.delete(0.0, END)
        self.rdo1.set(None)
        self.chk1.set(False)
        self.chk2.set(False)
        self.chk3.set(False)
        self.chk4.set(False)
        self.entryName.delete(0, END)
        self.entryAge.delete(0, END)
        self.entryLocale.delete(0, END)


def main():
    root = Tk()
    root.geometry('1000x550')
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
