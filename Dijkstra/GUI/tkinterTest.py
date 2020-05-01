import tkinter as tk

window = tk.Tk()
window.geometry("500x400")
window.title("Dijkstra Algorithm")
window.resizable(False, False)
window.configure(background="#eee")


def hello():
    txt = "Hello World!"
    lbl = tk.Label(window, text=txt)
    lbl.grid(row=0, column=1, sticky="W")


def hello_twice():
    txt = "Hello People"
    lbl = tk.Label(window, text=txt, fg="red", font=("Arial", 16))
    lbl.grid(row=1, column=1, sticky="W")


btn = tk.Button(text="Saluta!", command=hello)
btn.grid(row=0, column=0, sticky="W")

btn2 = tk.Button(text="Risaluta!", command=hello_twice)
btn2.grid(row=1, column=0, sticky="W")


if __name__ == "__main__":
    window.mainloop()
