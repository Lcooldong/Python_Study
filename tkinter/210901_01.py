import pygame.mixer
from tkinter import *

mixer = pygame.mixer
mixer.init()
track = mixer.Sound('./SoundFile/50459_M_RED_Nephlimizer.wav')

app = Tk()
app.title('Mix')
app.geometry('250x100+200+100')

start = Button(app, command=lambda: track.play(loops=-1), text='start')
start.pack(side=LEFT)

stop = Button(app, command=lambda: track.stop(), text='stop')
stop.pack(side=RIGHT)

app.mainloop()