import math

# Implementazione del grafo:
# TODO: Implementare una parte grafina per gestire meglio l'input del grafo.
grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["d"] = 8

grafo["a"] = {}
grafo["a"]["b"] = 6
grafo["a"]["c"] = 2

grafo["b"] = {}
grafo["b"]["end"] = 5

grafo["c"] = {}
grafo["c"]["d"] = 2
grafo["c"]["e"] = 9

grafo["d"] = {}
grafo["d"]["e"] = 3

grafo["e"] = {}
grafo["e"]["end"] = 1

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 2
costoNodi["b"] = math.inf
costoNodi["c"] = math.inf
costoNodi["d"] = 8
costoNodi["e"] = math.inf
costoNodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["d"] = "start"
parents["e"] = None
parents["end"] = None

processati = []


def nodo_con_costo_minore(costo_nddi):
    costoMinimo = math.inf  # Costo minimo del nodo attuale. [Ovviamente non è ancora stato calcoalto]
    nodoConCostoMinimo = None  # Nodo con il costo minimo. Verrà preso in considerazione per il percorso.

    for n in costoNodi:
        costoSingoloNodo = costoNodi[n]  # costo del nodo attuale.
        if (costoSingoloNodo < costoMinimo) and (n not in processati):
            costoMinimo = costoSingoloNodo  # Assegno come costo minimo il costo el nodo appena analizzato.
            nodoConCostoMinimo = n  # Assegno Il nodo con l'effettivo costo minimo alla variabile.

    return nodoConCostoMinimo  # Restituisco il nodo effettivo col costo minimo.


nodo = nodo_con_costo_minore(costoNodi)  # La funzione restituisce il nodo con costo minore.

while nodo is not None:
    costoNodo = costoNodi[nodo]  # costo nodo corrente.
    vicini = grafo[nodo]  # ricavo i nodi vicini
    for n in vicini.keys():
        nuovoCostoNodo = costoNodo + vicini[n]  # costo per arrivare al nodo che sto esaminando.
        if costoNodi[n] > nuovoCostoNodo:
            costoNodi[n] = nuovoCostoNodo
            parents[n] = nodo
    processati.append(nodo)  # inserisco il nodo appena processato in questo array in modo da non creare loop.
    nodo = nodo_con_costo_minore(costoNodi)


def rielaboraPercorso():  # Funzione per rielaborare l'array parents e restituire il percorso effettivo.
    val = reversed(parents.values())
    tmp = None
    out = []

    for item in val:
        if item == tmp:
            out.append(parents[item])
            break
        else:
            out.append(item)
            tmp = item
    return out


def getLastNode():  # Funzione "brutta" ma funzionale. Ci da l'ultima chiave dell'HashTable parents -> Il nodo finale.
    tmp = ""
    for item in parents.keys():
        tmp = item

    return tmp


def stampaPercorso(route):  # Da in out il percorso vero e proprio sottoforma di stringa umanamente leggibile.
    routeF = ""
    for item in reversed(route):
        routeF += item + " -> "

    routeF += getLastNode()
    return routeF.upper()


# TODO: Verificare che l'output funzioni su altri esempi di algoritmi.
print("ROUTE: ", stampaPercorso(rielaboraPercorso()))
