import tkinter as tk
from tkinter import *
from Dijkstra.Algorithm.Interface import Interface

# Configurazione gui
win = tk.Tk()
win.geometry("550x400")
win.title("Dijkstra Algorithm GUI")
win.resizable(False, False)
win.configure(background="#eee")


# ---------------------------------------------
# Funzioni per interazione
def addNodo():
    if txtInNomeNodo.get():
        nomeNodo = txtInNomeNodo.get()
        lstNodi.insert("end", nomeNodo)
        txtInNomeNodo.delete(0, "end")

        Interface.createNode(nomeNodo)  # Creazione del nodo.
    else:
        tk.messagebox.showinfo("Avviso", "Il valore inserito non è valido!")


def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('Item selezionato => { %d : "%s" } ' % (index, value))
    lblSelNodo = tk.Label(win, text=("Nodo selezionato: %s" % value), font=("arial", 12))
    lblSelNodo.grid(row=1, column=1, pady=20, sticky="N")


# ---------------------------------------------

# Row 0
# Label NomeNodo
lblNomeNodo = tk.Label(text="Inserire il nome del nodo:", font=("arial", 12))
lblNomeNodo.grid(row=0, column=0, sticky="W")

# Input NomeNodo
txtInNomeNodo = tk.Entry(font=("arial", 12))
txtInNomeNodo.grid(row=0, column=1, padx=10, sticky="W")

# Button AddNodo
btnAddNodo = tk.Button(text="Aggiungi nodo", font=("arial", 12), command=addNodo)
btnAddNodo.grid(row=0, column=2, padx=10, sticky="W")

# Row 1
# ListBox Nodi
lstNodi = tk.Listbox(win, height=15, width=25, selectmode=EXTENDED)
lstNodi.grid(row=1, column=0, pady=20, sticky="W")
lstNodi.bind('<<ListboxSelect>>', onselect)


# Funzione di avvio
if __name__ == "__main__":
    win.mainloop()
