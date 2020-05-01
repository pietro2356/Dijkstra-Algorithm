import tkinter as tk

# Configurazione gui
win = tk.Tk()
win.geometry("550x400")
win.title("Dijkstra Algorithm GUI")
win.resizable(False, False)
win.configure(background="#eee")


# ---------------------------------------------
# Funzioni per interazione
def addNodo():
    pass
    # Inserirli nel ListBox


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
lstNodi = tk.Listbox(win, height=15, width=25)
lstNodi.grid(row=1, column=0, pady=20, sticky="W")


if __name__ == "__main__":
    win.mainloop()
