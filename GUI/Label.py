import tkinter
from tkinter import Label
from tkinter import *

class MyLabel(tkinter.Label):
    anchor     = W
    justify    = LEFT
    wraplength = 300
    def __init__(self, _parent):
        tkinter.Label.__init__(self, _parent, anchor=MyLabel.anchor, justify=MyLabel.justify, wraplength=MyLabel.wraplength)

    def setText(self, text):
        self['text'] = text
