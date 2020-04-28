import math


# Implementazione del grafo:
# TODO: Implementare una parte grafina per gestire meglio l'input del grafo.
# --------------------------------------------------------------------------

# QUI VA MESSO IL CODICE RAPPRESENTANTE IL GRAFO DA ANALIZZARE.
# TROVI LA QUIDA NEL FILE 'GRAPH.md'.

# --------------------------------------------------------------------------

# TODO: Verificare il funzionamento una volta finito il tutto.
class Dijkstra:
    grafo = {}
    costoNodi = {}
    parents = {}
    processati = []

    @staticmethod
    def __init__(_grafo, _costoNodi, _parents, type):
        Dijkstra.grafo = _grafo
        Dijkstra.costoNodi = _costoNodi
        Dijkstra.parents = _parents

        Dijkstra.run()

        if type == 0:
            Dijkstra.result()
        elif type == 1:
            Dijkstra.resultGUI()
        else:
            pass

    @staticmethod
    def nodo_con_costo_minore():
        costoMinimo = math.inf  # Costo minimo del nodo attuale. [Ovviamente non è ancora stato calcoalto]
        nodoConCostoMinimo = None  # Nodo con il costo minimo. Verrà preso in considerazione per il percorso.

        for n in Dijkstra.costoNodi:
            costoSingoloNodo = Dijkstra.costoNodi[n]  # costo del nodo attuale.
            if (costoSingoloNodo < costoMinimo) and (n not in Dijkstra.processati):
                costoMinimo = costoSingoloNodo  # Assegno come costo minimo il costo el nodo appena analizzato.
                nodoConCostoMinimo = n  # Assegno Il nodo con l'effettivo costo minimo alla variabile.

        return nodoConCostoMinimo  # Restituisco il nodo effettivo col costo minimo.

    @staticmethod
    def run():
        nodo = Dijkstra.nodo_con_costo_minore()  # La funzione restituisce il nodo con costo minore.
        while nodo is not None:
            costoNodo = Dijkstra.costoNodi[nodo]  # costo nodo corrente.
            vicini = Dijkstra.grafo[nodo]  # ricavo i nodi vicini
            for n in vicini.keys():
                x = str(n)
                nuovoCostoNodo = costoNodo + vicini[x]  # costo per arrivare al nodo che sto esaminando.
                if Dijkstra.costoNodi[x] > nuovoCostoNodo:
                    Dijkstra.costoNodi[x] = nuovoCostoNodo
                    Dijkstra.parents[x] = nodo
            Dijkstra.processati.append(nodo)  # inserisco il nodo appena processato in questo array in modo da non creare loop.
            nodo = Dijkstra.nodo_con_costo_minore()

    @staticmethod
    def getLastNode():  # Funzione "brutta" ma funzionale. Ci da l'ultima chiave dell'HashTable parents -> Il nodo finale.
        tmp = ""
        for item in Dijkstra.parents.keys():
            tmp = item
        return tmp

    @staticmethod
    def getFirstNode():  # Funzione "brutta" ma funzionale. Ci da la prima chiave dell'HashTable parents -> Il nodo iniziale.
        for item in Dijkstra.grafo.keys():
            return item

    @staticmethod
    def stampaPercorso():
        # Separiamo le chiavi ed i rispettivi valori in due vettori differenti.
        val = []
        key = []
        outTMP = []
        for item in Dijkstra.parents.keys():
            key.append(item)
        for item in Dijkstra.parents.values():
            val.append(item)
        # Debug:
        # print("KEY: ", key)
        # print("VAL: ", val)

        a = len(key) - 1
        i = 0
        x = a
        while i < a:  # Creazione dell'output definitivo per il percorso da seguire.
            try:
                v = val[x]
                outTMP.append(v)
                x = key.index(v)
            except:
                break
            i += 1

        out = ""
        for item in range(len(outTMP) - 1, -1, -1):
            out += outTMP[item] + " -> "
        out += Dijkstra.getLastNode()
        return out.upper()

    @staticmethod
    def result():
        print("Grafo: ", Dijkstra.grafo)
        print("Parents: ", Dijkstra.parents)
        print("Percorso: ", Dijkstra.stampaPercorso())

    @staticmethod
    def resultGUI():
        return [Dijkstra.grafo, Dijkstra.parents, Dijkstra.stampaPercorso()]
