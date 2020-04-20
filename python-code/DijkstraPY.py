import math

# Implementazione del grafo:
# TODO: Implementare una parte grafina per gestire meglio l'input del grafo.
grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 2
grafo["start"]["b"] = 2
grafo["start"]["c"] = 4

grafo["a"] = {}
grafo["a"]["d"] = 8

grafo["b"] = {}
grafo["b"]["c"] = 1
grafo["b"]["end"] = 7

grafo["c"] = {}
grafo["c"]["end"] = 1

grafo["d"] = {}
grafo["d"]["end"] = 2

grafo["end"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["a"] = 2
costoNodi["b"] = 2
costoNodi["c"] = 4
costoNodi["d"] = math.inf
costoNodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "start"
parents["d"] = None
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


def getFirstNode():
    for item in grafo.keys():
        return item


def stampaPercorso(route):  # Da in out il percorso vero e proprio sottoforma di stringa umanamente leggibile.
    # routeF = getFirstNode() + " -> "
    routeF = ""
    for item in reversed(route):
        routeF += item + " -> "

    routeF += getLastNode()
    return routeF.upper()


def reloadRoute():
    # Separiamo le chiavi ed i rispettivi valori in due vettori differenti.
    val = []
    key = []
    outTMP = []
    for item in parents.keys():
        key.append(item)
    for item in parents.values():
        val.append(item)
    # Debug:
    print("KEY: ", key)
    print("VAL: ", val)

    tmp = 0
    for i in range(len(key) - 1, -1, -1):
        if tmp == 0:
            if val[i] == key[i - 1]:
                outTMP.append(val[i])
            elif val[i] != key[i - 1]:
                # outTMP.append(key[i - 2])
                # outTMP.append(val[i - 2])
                tmp = i
                # TODO: Sistemare l'output! In attesa di Help!
                continue
        else:
            outTMP.append(val[tmp])
            break

    out = "start"
    for item in range(len(outTMP) - 1, -1, -1):
        out += " -> " + outTMP[item]
    out += " -> end"
    return out.upper()


# TODO: Verificare che l'output funzioni su altri esempi di algoritmi.
print("Grafo: ", grafo)
print("Parents: ", parents)
print("red: ", reloadRoute())
# print("ROUTE: ", stampaPercorso(rielaboraPercorso()))
