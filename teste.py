from componentes import ChooseData
import tkinter as tk

win = tk.Tk()
win.resizable(False, False)
data = ChooseData(win, "Data Nascimento:")
data.pack()
# data.set("2/2/2000")
win.mainloop()