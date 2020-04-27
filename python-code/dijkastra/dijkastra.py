from tkinter import *

root = Tk()
root.title("Dijkastra Algorithm")
root.geometry('400x300')

lbl = Label(root, text="Nome Nodo: ").grid(column=0, row=0, padx=10, pady=10)

content = StringVar()
txt = Entry(root, textvariable=content)
txt.grid(column=1, row=0, pady=10)
txt.focus()


def collegamenti():
    lbl3 = Label(root, text="Collegato a: ")
    lbl3.grid(column=1, row=2, pady=30, sticky=N)
    content2 = StringVar()
    txt2 = Entry(root, textvariable=content2)
    txt2.grid(column=2, row=2, pady=30, sticky=N)
    txt2.focus()


def peso():
    lbl3 = Label(root, text="Peso: ")
    lbl3.grid(column=1, row=2, pady=50, sticky=N)
    content3 = StringVar()
    txt3 = Entry(root, textvariable=content3)
    txt3.grid(column=2, row=2, pady=50, sticky=N)


def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))
    lbl2 = Label(root, text=("Nodo '%s'" % value))
    lbl2.grid(column=1, row=2, pady=10, sticky=N)
    collegamenti()
    peso()


listbox = Listbox(root, selectmode=EXTENDED)
listbox.grid(column=0, row=2, pady=10)
listbox.bind('<<ListboxSelect>>', onselect)


def addnode():
    listbox.insert("end", content.get())
    txt.delete(0, "end")


btn = Button(root, text="+ New Nodo", command=addnode)
btn.grid(column=0, row=1, pady=5)

calcolo = Button(root, text="Calcolo Percorso", command=addnode)
calcolo.grid(column=1, row=3, pady=5)
root.mainloop()