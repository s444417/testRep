from Api.RelatedCollection import RelatedCollection
from Api.Related import Related
from GUI.Label import MyLabel
from GUI.DoubleEntryAndButton import DoubleEntryAndButton
from GUI.DoubleLabelAndButton import DoubleLabelAndButton
import tkinter
from tkinter import messagebox
from tkinter import *

class App:
    def __init__(self):
        #MyLabel.wraplength = 30
        self.relatedCollectionR = RelatedCollection()
        self.relatedCollectionS = RelatedCollection()
        window = tkinter.Tk()
        window.title("Projekt LiTM")
        self.panelR = DoubleEntryAndButton(window, self.onAddR, 'R', 0)
        self.panelS = DoubleEntryAndButton(window, self.onAddS, 'S', 2)
        self.result = DoubleLabelAndButton(window, self.onClean, 4)
        window.mainloop()

    def onAddR(self, left, right):
        self.onAdd(left, right, 'R', self.relatedCollectionR, self.panelR)

    def onAddS(self, left, right):
         self.onAdd(left, right, 'S', self.relatedCollectionS, self.panelS)
                
    def onAdd(self, left, right, relationName, relatedCollection, panel):
        if(left != '' and right !=''):
            if(relatedCollection.canAdd(left, right)):
                relatedCollection + Related(left, right)
                panel.setText(relationName + relatedCollection.toString())        
                self.result.setText(
                'S◦R' + (self.relatedCollectionR * self.relatedCollectionS).toString(),
                'R◦S' + self.relatedCollectionS.getComposition(self.relatedCollectionR).toString())
            else:
                messagebox.showinfo("Błąd", "Ten element znajduje się już na liście!")
        else:
            messagebox.showinfo("Błąd", "Element nie może być pusty!")

    def onClean(self):
        #self.panelR.__doCleanEntries()
        self.relatedCollectionR.clear()
        self.relatedCollectionS.clear()
        self.result.doClean()
        self.panelR.doClean()
        self.panelS.doClean()        
            
App()

