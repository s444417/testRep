from GUI.Label import MyLabel
from GUI.Entry import MyEntry
from GUI.Button import MyButton
from GUI.Cleaneable import Cleaneable
import tkinter
from tkinter import *

class DoubleEntryAndButton(Cleaneable):
    def __init__(self, parent, onAddAction, name, num):
        self.onAddAction = onAddAction
        self.resultLabel = MyLabel(parent)
        self.entryLeft  = MyEntry(parent)
        self.entryRight = MyEntry(parent)
        self.__createInputs(parent, num, name)

    def __onClickAction(self):
        self.onAddAction(self.entryLeft.getText(), self.entryRight.getText())
        self.__doCleanEntries()

    def __createInputs(self, parent, num, relationName):
        num = num + 1        
        label1 = tkinter.Label(parent, text = relationName + "( ")
        label2 = tkinter.Label(parent, text = ", ")
        label3 = tkinter.Label(parent, text = " )")

        buttonAdd = MyButton(parent, "dodaj", self.__onClickAction)
        label1.grid(row = num, column = 0, sticky = E)
        self.entryLeft.grid(row = num, column = 1)
        label2.grid(row = num, column = 2)
        self.entryRight.grid(row = num, column = 3)
        label3.grid(row = num, column = 4)
        buttonAdd.grid(row = num, column = 5)
        self.resultLabel.grid(row = num - 1, columnspan = 5, sticky = W)
    
    def __doCleanEntries(self):
        self.entryLeft.delete(0, 'end')
        self.entryRight.delete(0, 'end')

    def doClean(self):
        self.setText('')
        self.__doCleanEntries()

    def setText(self, text):
        self.resultLabel.setText(text)

    
