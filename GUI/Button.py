import tkinter
from tkinter import Button

class MyButton(tkinter.Button):
    def __init__(self, _parent, name, onClickAction):
        tkinter.Button.__init__(self, _parent, text = name)
        self['command'] = lambda : onClickAction()
