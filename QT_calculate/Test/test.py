from tkinter import *

win = Tk()
win.title("Game")
win.geometry("500x200")


def press(event):
    global txt
    txt = event


win.bind("<KeyPress>", press)

cvs = Canvas(win)
cvs.config(width=500, height=200, bd=0, highlightthicknes=0)
p1 = (250, 100)
txt = ''
event_txt = cvs.create_text(p1, text=txt, font=("Arial", 10))
cvs.pack()

win.update()

while True:
    cvs.delete(event_txt)
    event_txt = cvs.create_text(p1, text=txt, font=("Arial", 10))
    win.update()

# win.mainloop()

