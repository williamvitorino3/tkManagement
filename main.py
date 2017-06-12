import tkinter as tk
from view.tela import Janela


root = tk.Tk()
root.title("tkMed")
root.resizable(False, False)
root.geometry("1366x768+0+0")
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
tela = Janela(root)
root.mainloop()
