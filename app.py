
from tkinter import Tk
#import tkinter as Tk

app = Tk()
app.iconbitmap("App/images/icone.ico")
app['bg'] = "gray"
app.title("Primeira App")
app.geometry("500x200")
app.resizable(True, True)
app.minsize(500, 200)
app.maxsize(700, 400)

btn = button(app, text="Executar")
btn.pack()
app.mainloop()
