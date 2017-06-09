from tkinter import *
from tkinter import ttk
from componentes import CustomCombobox as ccb

class App:

    value_of_combo = 'X'

    def __init__(self, parent):
        self.parent = parent
        self.combo()

    def mostrar(self, event):
        print(self.box_value.get())

    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value)
        self.box['values'] = ('X', 'Y', 'Z')
        self.box.current(0)
        self.box.bind("<<ComboboxSelected>>", self.mostrar)
        self.box.pack()

if __name__ == '__main__':
    root = Tk()
    root.mainloop()