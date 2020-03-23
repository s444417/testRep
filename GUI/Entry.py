import tkinter
from tkinter import Entry
from tkinter import StringVar

class MyEntry(tkinter.Entry):
    def __init__(self, _parent):
        self.stringVar = StringVar()
        tkinter.Entry.__init__(self, _parent, textvariable = self.stringVar)

    def getText(self):
        return self.stringVar.get().strip()
