from tkinter import *
from datetime import datetime

win = Tk()
win.title("Game")
win.geometry("2000x500")


def press(event):
    global right_go, t_0
    if event.keysym == "space" and right_go != True:
        right_go = True
        t_0 = datetime.now()


right_go = False
win.bind("<KeyPress>", press)

cvs = Canvas(win)
cvs.config(width=2000, height=500, bd=0, highlightthicknes=0)
p1 = (0, 200)
p2 = (100, 300)
sqr = cvs.create_rectangle(p1, p2, fill="yellow")
velo = 2000/10
cvs.pack()

win.update()

while True:
    cvs.delete(sqr)
    if right_go == True:
        t_now = datetime.now()
        t_delta = (t_now-t_0).total_seconds()
        p1_x = round(0 + velo*t_delta)
        p2_x = p1_x + 100
        p1 = (p1_x, 200)
        p2 = (p2_x, 300)
    sqr = cvs.create_rectangle(p1, p2, fill="yellow")
    win.update()

# win.mainloop()

