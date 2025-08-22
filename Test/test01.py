from tkinter import *
from tkinter import ttk

mensaje = "Prueba en el nuevo repositorio"

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text = mensaje).grid(column=0,row=0)
ttk.Button(frame, text="Prueba"). grid(column=0, row=1)
root.mainloop()