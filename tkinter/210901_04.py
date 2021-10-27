from tkinter import *


class Application(Frame):
    def __init__(self, up):
        Frame.__init__(self, up)
        self.grid()

        self.clk = 0

        self.btn1 = Button(self, text='Total Click: 0')
        self.btn1['command'] = self.update
        self.btn1.grid()
    
    def update(self):
        self.clk = self.clk + 1
        self.btn1['text'] = f'Total Clicks: {str(self.clk)}'


app = Tk()
app.title('simple GUI 1')
app.geometry('200x100')

top = Application(app)

app.mainloop()


