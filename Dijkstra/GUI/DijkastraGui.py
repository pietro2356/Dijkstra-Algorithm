from tkinter import *
from Dijkstra.Algorithm.Interface import Interface


class GUI(object):
    app = Tk()
    app.title("Dijkastra Algorithm")
    app.geometry('400x300')

    lbl = Label(app, text="Nome Nodo: ").grid(column=0, row=0, padx=10, pady=10)

    content = StringVar()
    txt = Entry(app, textvariable=content)
    txt.grid(column=1, row=0, pady=10)
    txt.focus()

    # TODO: Da reimplementare.
    RAM = []

    def collegamenti(self):
        lbl3 = Label(GUI.app, text="Collegato a: ")
        lbl3.grid(column=1, row=2, pady=30, sticky=N)
        content2 = StringVar()
        txt2 = Entry(GUI.app, textvariable=content2)
        txt2.grid(column=2, row=2, pady=30, sticky=N)
        txt2.focus()
        print(txt2.get())
        return txt2.get()

    def peso(self):
        lbl3 = Label(GUI.app, text="Peso: ")
        lbl3.grid(column=1, row=2, pady=50, sticky=N)
        content3 = StringVar()
        txt3 = Entry(GUI.app, textvariable=content3)
        txt3.grid(column=2, row=2, pady=50, sticky=N)
        txt3.focus()
        print(txt3.get())
        return txt3.get()

    def onselect(evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item %d: "%s"' % (index, value))
        lbl2 = Label(GUI.app, text=("Nodo '%s'" % value))
        # Value ==> nodoStart
        lbl2.grid(column=1, row=2, pady=10, sticky=N)

        GUI.RAM.append({value, GUI.collegamenti(), GUI.peso()})
        # collegamenti()
        # peso()

    listbox = Listbox(app, selectmode=EXTENDED)
    listbox.grid(column=0, row=2, pady=10)
    listbox.bind('<<ListboxSelect>>', onselect)

    def addnode(self):
        listbox.insert("end", GUI.content.get())
        txt.delete(0, "end")
        Interface.createNode(GUI.content.get())

    def update(self):
        print("Out RAM")
        for i in GUI.RAM:
            print(i)

    # TODO: Reimplementare il tutto con una classe.
    btn = Button(app, text="+ New Nodo", command=addnode(""))
    btn.grid(column=0, row=1, pady=5)

    calcolo = Button(app, text="Calcolo Percorso", command=Interface.run())
    calcolo.grid(column=1, row=3, pady=5)
    update = Button(app, text="Aggiorna", command=update)
    update.grid(column=2, row=3, pady=5)
    app.mainloop()
