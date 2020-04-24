import math
from Algorithm.Dijkstra import Dijkstra


class CliInterface:
    grafo = {}
    costoNodi = {}
    parents = {}

    nodoStart = ""

    @staticmethod
    def __init__(self):
        print("N° nodi: ")
        nNodi = int(input())

        # Inserimento dei nodi:
        for i in range(0, nNodi):
            print("Inserisci il valore del nodo: ", i)
            CliInterface.createNode(input())

        print("GRAFO: ", CliInterface.grafo)

        # Inserimento dei link:
        while True:
            try:
                print("Inserisci il nodo di partenza: ")
                nP = input()
                print("Inserisci il nodo di arrivo: ")
                nA = input()
                print("Inserisci il peso del link: ")
                p = int(input())

                CliInterface.setLink(nP, nA, p)
                # TODO: Continuare che funziona.
                print("Continuare? [0 or 1]")
                if int(input()) == 0:
                    break
                else:
                    continue
            except KeyError:
                print("Valore non corretto!")
                continue
        print("GRAFO: ", CliInterface.grafo)

        # Imposto il costo dei nodi:
        print("Indicare il nodo di partenza: ")
        nS = input()
        vicini = CliInterface.grafo[nS]
        print(vicini)
        CliInterface.setCostoNodi(nS, 0)    # Il costo del nodo di partenza è sempre 0.

        for item in vicini.keys():
            peso = vicini[item]
            print(item + ":" + str(peso))
            # Imposto il peso dei nodi direttamente collegati al nodo sorgente
            CliInterface.setCostoNodi(item, peso)
            # Imposto il parent dei nodi direttamente collegati al nodo sorgente
            CliInterface.setParent(item, nS)

        print("Costo nodi DEG: ", CliInterface.costoNodi)

        for item in CliInterface.grafo:
            if item not in CliInterface.costoNodi:
                # Impostiamo ad Inf i nodi NON direttamente collegati al nodo sorgente.
                CliInterface.setCostoNodi(item, math.inf)
                # Impostiamo a None i nodi NON direttamente collegati al nodo sorgente.
                CliInterface.setParent(item, None)
        print("Costo nodi: ", CliInterface.costoNodi)

        # Impostazione dei parenti:


        # Esecuzione algoritmo
        Dijkstra.__init__(CliInterface.grafo,
                          CliInterface.costoNodi,
                          CliInterface.parents)

    @staticmethod
    def createNode(nomeNodo):
        CliInterface.grafo[nomeNodo] = {}

    @staticmethod
    def setLink(nodoStart, nodoEnd, peso):
        CliInterface.grafo[nodoStart][nodoEnd] = peso

    @staticmethod
    def setStartNode(nomeNodo):
        CliInterface.nodoStart = nomeNodo

    @staticmethod
    def setCostoNodi(nodo, peso):
        CliInterface.costoNodi[nodo] = peso

    @staticmethod
    def setParent(nodo, parent):
        CliInterface.parents[nodo] = parent

