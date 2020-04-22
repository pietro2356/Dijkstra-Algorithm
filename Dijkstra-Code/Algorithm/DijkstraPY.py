import math

# Implementazione del grafo:
# TODO: Implementare una parte grafina per gestire meglio l'input del grafo.
grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["d"] = 8

grafo["a"] = {}
grafo["a"]["c"] = 2
grafo["a"]["b"] = 6

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


def getLastNode():  # Funzione "brutta" ma funzionale. Ci da l'ultima chiave dell'HashTable parents -> Il nodo finale.
    tmp = ""
    for item in parents.keys():
        tmp = item
    return tmp


def getFirstNode():  # Funzione "brutta" ma funzionale. Ci da la prima chiave dell'HashTable parents -> Il nodo iniziale.
    for item in grafo.keys():
        return item


def stampaPercorso():
    # Separiamo le chiavi ed i rispettivi valori in due vettori differenti.
    val = []
    key = []
    outTMP = []
    for item in parents.keys():
        key.append(item)
    for item in parents.values():
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
    out += "end"
    return out.upper()


# print("Grafo: ", grafo)
# print("Parents: ", parents)
print("Percorso: ", stampaPercorso())
