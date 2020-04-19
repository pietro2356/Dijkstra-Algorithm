import math

# Implementazione del grafo:
grafo = {}
grafo["start"] = {}
grafo["start"]["a"] = 6
grafo["start"]["b"] = 2

grafo["a"] = {}
grafo["a"]["end"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["end"] = 5

grafo["end"] = {}

# Tabella costi:
costo_nodi = {}
costo_nodi["a"] = 6
costo_nodi["b"] = 2
costo_nodi["end"] = math.inf

# Tabella parents:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processati = []


def nodo_con_costo_minore(costo_nddi):
    costo_minimo = math.inf         # Costo minimo del nodo attuale. [Ovviamente non è ancora stato calcoalto]
    nodo_con_costo_minimo = None    # Nodo con il costo minimo. Verrà preso in considerazione per il percorso.

    for n in costo_nodi:
        costo_nodo = costo_nodi[n]  # costo del nodo attuale.
        if (costo_nodo < costo_minimo) and (n not in processati):
            costo_minimo = costo_nodo   # Assegno come costo minimo il costo el nodo appena analizzato.
            nodo_con_costo_minimo = n   # Assegno Il nodo con l'effettivo costo minimo alla variabile.

    return nodo_con_costo_minimo    # Restituisco il nodo effettivo col costo minimo.


nodo = nodo_con_costo_minore(costo_nodi)    # La funzione restituisce il nodo con costo minore.

while nodo is not None:
    costo_nodo = costo_nodi[nodo]   # costo nodo corrente.
    vicini = grafo[nodo]    # ricavo i nodi vicini
    for n in vicini.keys():
        nuovo_costo_nodo = costo_nodo + vicini[n]   # costo per arrivare al nodo che sto esaminando.
        if costo_nodi[n] > nuovo_costo_nodo:
            costo_nodi[n] = nuovo_costo_nodo
            parents[n] = nodo
    processati.append(nodo)     # inserisco il nodo appena processato in questo array in modo da non creare loop.
    nodo = nodo_con_costo_minore(costo_nodi)

print(parents)