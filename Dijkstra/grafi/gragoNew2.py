import math

grafo = {}
grafo["A"] = {}
grafo["A"]["B"] = 2
grafo["A"]["C"] = 4

grafo["B"] = {}
grafo["B"]["D"] = 8
grafo["B"]["C"] = 7

grafo["C"] = {}
grafo["C"]["D"] = 9

grafo["D"] = {}

# Tabella costi:
costoNodi = {}
costoNodi["A"] = 0
costoNodi["B"] = 2
costoNodi["C"] = 4
costoNodi["E"] = math.inf


# Tabella parents:
parents = {}
parents["B"] = "A"
parents["C"] = "A"
parents["D"] = None

processati = []

print("GRAFO:", grafo)
print("COSTO NODI:", costoNodi)
print("PARENTS:", parents)