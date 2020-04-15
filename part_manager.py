from tkinter import *


def populate_list():
    print("Populate")


def add_item():
    print("Adicionar")


def remove_item():
    print("Remover")


def update_item():
    print("Actualizar")


def clear_text():
    print("Apagar registo")


# Create window object
app = Tk()

# Part
part_text = StringVar()
part_label = Label(app, text="Componente", pady="20")
part_label.grid(row=0, column=0, sticky=W)
partEntry = Entry(app, textvar=part_text)
partEntry.grid(row=0, column=1)

# Customer
costumer_text = StringVar()
costumer_label = Label(app, text="Cliente")
costumer_label.grid(row=0, column=2, sticky=W)
costumerEntry = Entry(app, textvar=costumer_text)
costumerEntry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_label = Label(app, text="Retalhista")
retailer_label.grid(row=1, column=0, sticky=W)
retailerEntry = Entry(app, textvar=retailer_text)
retailerEntry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_label = StringVar()
price_label = Label(app, text="Preço")
price_label.grid(row=1, column=2, sticky=W)
priceEntry = Entry(app, textvar=price_text)
priceEntry.grid(row=1, column=3)

# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=50)
parts_list.grid(row=3, column=0, padx=20, pady=20, columnspan=3, rowspan=6)
app.title("Part Manager")
app.geometry("700x350")

# Buttons
add_btn = Button(app, text="Adicionar componente", width=20, command=add_item)
add_btn.grid(row=2, column=0, pady=20)
remove_btn = Button(app, text="Remover componente",
                    width=20, command=remove_item)
remove_btn.grid(row=2, column=1, padx=10)
update_btn = Button(app, text="Actualizar componente",
                    width=20, command=update_item)
update_btn.grid(row=2, column=2, padx=5)
clear_btn = Button(app, text="Apagar registo", width=20, command=clear_text)
clear_btn.grid(row=2, column=3, padx=5)
# Start program
app.mainloop()
