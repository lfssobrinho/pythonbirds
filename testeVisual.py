#!/usr/local/bin/python
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = Button(self, text="Sair", command=self.quit)
        self.quitButton.grid()



app = Application()
app.master.title("Sample application")
app.mainloop()
