import math
from Algorithm.Dijkstra import Dijkstra


class CliInterface:
    grafo = {}
    costoNodi = {}
    parents = {}
    processati = []

    nodoStart = ""

    @staticmethod
    def __init__(self):
        print("N° nodi: ")
        nNodi = int(input())

        for i in range(0, nNodi):
            print("Inserisci il valore del nodo: ", i)
            CliInterface.createNode(input())

        print(CliInterface.grafo)

        while True:
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

        print(CliInterface.grafo)
        Dijkstra.__init__(self)

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
    def setCostoNodi():
        for i in CliInterface.grafo:
            print("Costo del nodo: ", i)
            CliInterface.costoNodi[i] = input()


