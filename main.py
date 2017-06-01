import tkinter as tk
from tela import Janela


root = tk.Tk()
root.title("tkMed")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
tela = Janela(root)
root.mainloop()
