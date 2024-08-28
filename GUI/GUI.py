from tkinter import *
import tkinter as tk
from functions import *
import os

def removeDMGs():
    try:
        os.chdir(downloadsDirectory)
        array = getDMGFiles(downloadsDirectory)
        for file in array:
            os.remove(file)
        if len(getDMGFiles(downloadsDirectory)) == 0:
            statusLabel.config(text="Status: Removed all DMGs")
            listTextBox.delete(1.0, END)
            for i in getDMGFiles(downloadsDirectory):
                listTextBox.insert(END, i + "\n")
        else:
            statusLabel.config(text="Some still remain, try ADMIN mode")
    except Exception as E:
        pass
    
def removeDMGsSudo():
    try:
        os.chdir(downloadsDirectory)
        array = getDMGFiles(downloadsDirectory)
        for file in array:
            os.system(f"sudo rm -rf \"{file}\"")
        if len(getDMGFiles(downloadsDirectory)) == 0:
            statusLabel.config(text="Status: Removed all DMGs")
            listTextBox.delete(1.0, END)
            for i in getDMGFiles(downloadsDirectory):
                listTextBox.insert(END, i + "\n")
        else:
            statusLabel.config(text="Some still remain, error")
    except Exception as E:
        statusLabel.config(text=f"Error: {E}")
        print(f"An error occurred: {E}")


def refreshlist():
    listTextBox.delete(1.0, END)
    for i in getDMGFiles(downloadsDirectory):
        listTextBox.insert(END, i + "\n")

root = tk.Tk()
root.title("GUI DMG remover")

title = Label(root, text="DMG remover", font=("Arial", 30))
title.pack()

listTextBox = Text(root, height=15, width=60, font=("Arial", 18))
listTextBox.pack()
listTextBox.delete(1.0, END)

for i in getDMGFiles(downloadsDirectory):
    listTextBox.insert(END, i + "\n")


refreshList = Button(root, text="Refresh List", command=refreshlist, font=("Arial", 18))
refreshList.pack()

askRemoveSudo = Button(root, text="Remove DMGs (sudo)", command=removeDMGsSudo, font=("Arial", 18))
askRemoveSudo.pack()

removeAllButton = Button(root, text="Remove DMGs", command=removeDMGs, font=("Arial", 18))
removeAllButton.pack()

statusLabel = Label(root, text="Status: Ready", font=("Arial", 18))
statusLabel.pack()

root.mainloop()
