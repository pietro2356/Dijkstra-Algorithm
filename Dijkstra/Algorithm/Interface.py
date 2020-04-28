import math
from Dijkstra.Algorithm.Dijkstra import Dijkstra


class Interface:
    grafo = {}
    costoNodi = {}
    parents = {}

    nodoStart = ""

    # METODO PER INTERFACCIA A CLI
    @staticmethod
    def __init__(self):
        print("N° nodi: ")
        nNodi = int(input())

        # Inserimento dei nodi:
        for i in range(0, nNodi):
            print("Inserisci il valore del nodo: ", i)
            Interface.createNode(input())

        # print("GRAFO: ", Interface.grafo)

        # Inserimento dei link:
        while True:
            try:
                print("Inserisci il nodo di partenza: ")
                nP = input()
                print("Inserisci il nodo di arrivo: ")
                nA = input()
                print("Inserisci il peso del link: ")
                p = int(input())

                Interface.setLink(nP, nA, p)
                # TODO: Continuare che funziona.
                print("Continuare? [0 or 1]")
                if int(input()) == 0:
                    break
                else:
                    continue
            except KeyError:
                print("Valore non corretto!")
                continue
        # print("GRAFO: ", Interface.grafo)

        # Imposto il costo dei nodi e dei pearent:
        print("Indicare il nodo di partenza: ")
        nS = input()
        vicini = Interface.grafo[nS]
        # print(vicini)
        Interface.setCostoNodi(nS, 0)    # Il costo del nodo di partenza è sempre 0.

        for item in vicini.keys():
            peso = vicini[item]
            print(item + ":" + str(peso))
            # Imposto il peso dei nodi direttamente collegati al nodo sorgente
            Interface.setCostoNodi(item, peso)
            # Imposto il parent dei nodi direttamente collegati al nodo sorgente
            Interface.setParent(item, nS)

        # print("Costo nodi DEG: ", Interface.costoNodi)

        for item in Interface.grafo:
            if item not in Interface.costoNodi:
                # Impostiamo ad Inf i nodi NON direttamente collegati al nodo sorgente.
                Interface.setCostoNodi(item, math.inf)
                # Impostiamo a None i nodi NON direttamente collegati al nodo sorgente.
                Interface.setParent(item, None)
        # print("Costo nodi: ", Interface.costoNodi)

        # Esecuzione algoritmo
        Dijkstra.__init__(Interface.grafo,
                          Interface.costoNodi,
                          Interface.parents, 0)

    @staticmethod
    def createNode(nomeNodo):
        Interface.grafo[nomeNodo] = {}

    @staticmethod
    def setLink(nodoStart, nodoEnd, peso):
        Interface.grafo[nodoStart][nodoEnd] = peso

    @staticmethod
    def setStartNode(nomeNodo):
        Interface.nodoStart = nomeNodo

    @staticmethod
    def setCostoNodi(nodo, peso):
        Interface.costoNodi[nodo] = peso

    @staticmethod
    def setParent(nodo, parent):
        Interface.parents[nodo] = parent

    @staticmethod
    def run():
        Dijkstra.__init__(Interface.grafo,
                          Interface.costoNodi,
                          Interface.parents, 1)
