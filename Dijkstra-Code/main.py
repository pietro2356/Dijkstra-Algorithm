from Algorithm.DijkstraPY import *
from Algorithm.interfaceFunc import *

nNodi = 0

# TODO: Da sistemare.
def main():
    print("Programma esecuzione algoritmo Dijkstra!")
    print("Qunanti nodi servono?")
    tmp = input()
    if int(tmp) >= 0:
        nNodi = int(tmp)
    else:
        exit(500)

    for i in range(0, nNodi):
        print("Inserisci il nome del nodo ", i, ": ")
        tmpN = input()
        if type(tmpN) != 'str':
            createNewNodo(tmpN)
        else:
            exit(400)
    print(outNodi())

    print("Impostiamo i Link: ")
    while True:
        print("Seleziona il nodo di partenza: ")
        nP = input()
        print("Seleziona il nodo di arrivo: ")
        nE = input()
        print("Seleziona il peso del link: ")
        p = input()
        setLink(nP, nE, p)
        if KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
