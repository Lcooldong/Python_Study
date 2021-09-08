from tkinter import *


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("HOME")
        self.pack(fill=X)

        self.leftFrame = Frame(self, bg='black')
        self.leftFrame.pack(fill=BOTH, ipadx=40, ipady=200, side=LEFT)

        self.topLabel = Label(self.leftFrame)
        self.topLabel.pack(fill=BOTH, ipady=30)

        lbl1 = Label(self.leftFrame, text='10', width=20, height=2, bg='purple')
        lbl1.pack(fill=X, side=TOP)
        lbl2 = Label(self.leftFrame, text='10', width=20, height=2, bg='skyBlue')
        lbl2.pack(fill=X, side=TOP)
        lbl3 = Label(self.leftFrame, text='10', width=20, height=2, bg='magenta')
        lbl3.pack(fill=X, side=TOP)
        lbl4 = Label(self.leftFrame, text='10', width=20, height=2, bg='brown')
        lbl4.pack(fill=X, side=TOP)

        self.frame1 = Frame(self, bg='red')
        self.frame1.pack(fill=BOTH, ipady=40)
        self.frame2 = Frame(self, bg='orange')
        self.frame2.pack(fill=BOTH, ipady=8.5)
        self.frame3 = Frame(self, bg='yellow')
        self.frame3.pack(fill=BOTH, ipady=10)
        self.frame4 = Frame(self, bg='green')
        self.frame4.pack(fill=BOTH, ipady=10)
        self.frame5 = Frame(self, bg='blue')
        self.frame5.pack(fill=BOTH, ipady=10)
        self.frame6 = Frame(self, bg='darkBlue')
        self.frame6.pack(fill=BOTH, ipady=10)
        self.frame7 = Frame(self, bg='purple')
        self.frame7.pack(fill=BOTH, ipady=10)
        self.frame8 = Frame(self)
        self.frame8.pack(fill=BOTH, ipady=10)

        self.entryAge = Entry(self.frame2)
        self.entryAge.pack(side=LEFT)
        self.entryLocale = Entry(self.frame3)
        self.entryLocale.pack(side=LEFT)
        self.entryLocale = Entry(self.frame4)
        self.entryLocale.pack(side=LEFT)

        self.chk1 = BooleanVar()
        self.chk2 = BooleanVar()
        self.chk3 = BooleanVar()
        self.rdo1 = StringVar()
        self.rdo1.set(None)

        self.checkBtn1 = Checkbutton(self.frame5, text='Kendo', variable=self.chk1)
        self.checkBtn1.pack(side=LEFT)
        self.checkBtn2 = Checkbutton(self.frame5, text='Archery', variable=self.chk2)
        self.checkBtn2.pack(side=LEFT)
        self.checkBtn3 = Checkbutton(self.frame5, text='Making', variable=self.chk3)
        self.checkBtn3.pack(side=LEFT)

        self.r1 = Radiobutton(self.frame6, text='Kendo', variable=self.rdo1, value='sword')
        self.r1.pack(side=LEFT)
        self.r2 = Radiobutton(self.frame6, text='Archery', variable=self.rdo1, value='bow')
        self.r2.pack(side=LEFT)
        self.r3 = Radiobutton(self.frame6, text='Making', variable=self.rdo1, value='hammer')
        self.r3.pack(side=LEFT)

        self.confirmBtn = Button(self.frame7, text='Confirm', fg='#01F201', bg='#D212E2', command=self.update)
        self.confirmBtn.pack(side=LEFT, padx=50, ipadx=4, ipady=5)

        self.eraseBtn = Button(self.frame7, text='ERASE', fg='#01F201', bg='#D212E2', command=self.update)
        self.eraseBtn.pack(side=RIGHT, padx=50, ipadx=8, ipady=5)

        self.txt = Text(self.frame8, width=35, height=5, wrap=WORD)  # 리턴값 객체
        self.txt.pack(fill=BOTH, side=TOP)

        self.buttomFrame = Frame(self, bg='purple')
        self.buttomFrame.pack(fill=Y)

def main():
    root = Tk()
    root.geometry('1000x500')
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()