import math

# Implementazione del grafo:
# TODO: Implementare una parte grafina per gestire meglio l'input del grafo.
grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["b"] = 20
grafo["start"]["c"] = 10

grafo["a"] = {}
grafo["a"]["d"] = 4

grafo["b"] = {}
grafo["b"]["a"] = 0
grafo["b"]["d"] = 5
grafo["b"]["e"] = 4

grafo["c"] = {}
grafo["c"]["e"] = 2
grafo["c"]["f"] = 1

grafo["d"] = {}
grafo["d"]["i"] = 40
grafo["d"]["h"] = 20
grafo["d"]["e"] = 2

grafo["e"] = {}
grafo["e"]["l"] = 2
grafo["e"]["g"] = 1

grafo["f"] = {}
grafo["f"]["e"] = 8

grafo["g"] = {}
grafo["g"]["l"] = 5

grafo["h"] = {}
grafo["h"]["l"] = 1
grafo["h"]["k"] = 20

grafo["i"] = {}
grafo["i"]["j"] = 1

grafo["j"] = {}
grafo["j"]["m"] = 7
grafo["j"]["k"] = 14

grafo["k"] = {}
grafo["k"]["n"] = 7

grafo["l"] = {}
grafo["l"]["o"] = 2
grafo["l"]["end"] = 8

grafo["m"] = {}
grafo["m"]["n"] = 0

grafo["n"] = {}
grafo["n"]["end"] = 1

grafo["o"] = {}
grafo["o"]["end"] = 2

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 2
costoNodi["b"] = 20
costoNodi["c"] = 10
costoNodi["d"] = math.inf
costoNodi["e"] = math.inf
costoNodi["f"] = math.inf
costoNodi["g"] = math.inf
costoNodi["h"] = math.inf
costoNodi["i"] = math.inf
costoNodi["j"] = math.inf
costoNodi["k"] = math.inf
costoNodi["l"] = math.inf
costoNodi["m"] = math.inf
costoNodi["n"] = math.inf
costoNodi["o"] = math.inf
costoNodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "start"
parents["d"] = None
parents["e"] = None
parents["f"] = None
parents["g"] = None
parents["h"] = None
parents["i"] = None
parents["j"] = None
parents["k"] = None
parents["l"] = None
parents["m"] = None
parents["n"] = None
parents["o"] = None
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
