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

nodo = nodo_con_costo_minore(costo_nodi)    # La funzione restituisce il nodo con costo minore.

while nodo is not None:
    costo_nodo = costo_nodi[nodo]   # costo nodo corrente.
    vicini = grafo[nodo]    # ricavo i nodi vicini

    for n in vicini.keys():
        nuovo_costo_nodo = costo_nodo + vicini[n]   # costo per arrivare al nodo che sto esaminando.
                                                    # Partendo da start
        if costo_nodi[n] > nuovo_costo_nodo:
            costo_nodi[n] = nuovo_costo_nodo
            parents[n] = nodo

    processati.append(nodo)
    nodo = nodo_con_costo_minore(costo_nodi)
