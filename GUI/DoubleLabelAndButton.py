from GUI.Label import MyLabel
from GUI.Entry import MyEntry
from GUI.Button import MyButton
from GUI.Cleaneable import Cleaneable
import tkinter
from tkinter import *

class DoubleLabelAndButton(Cleaneable):
    def __init__(self, parent, onClickAction, num):
        self.resultLabelSR = MyLabel(parent)
        self.resultLabelRS = MyLabel(parent)
        self.__createInputs(parent, num, onClickAction)

    def __createInputs(self, parent, num, onClickAction):
        buttonClean = MyButton(parent, "czyść", onClickAction)        
        buttonClean.grid(row = num, column = 5, rowspan = 2)
        self.resultLabelSR.grid(row = num, columnspan = 5, sticky = W)
        self.resultLabelRS.grid(row = num + 1, columnspan = 5, sticky = W)

    def doClean(self):
        self.setText('', '')

    def setText(self, textSR, textRS):
        self.resultLabelSR.setText(textSR)
        self.resultLabelRS.setText(textRS)
