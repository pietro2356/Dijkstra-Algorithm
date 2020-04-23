# GUIDA ALLA CREAZIONE DEI GRAFI

#### IMMAGINE DEL GRAFO
![grafoStart](/img/grafoStart.png)

> **CREARE IL GRAFO PRINCIPALE**
```python
grafo = {}
```

> **CREARE I VARI NODI**
* I nodi saranno: S, A, B, C, D, E.
* Creiamo i **nodi** che ci serviranno:
```python
grafo["nome_nodo"] = {}
grafo["S"] = {}
grafo["A"] = {}
grafo["B"] = {}
grafo["C"] = {}
grafo["D"] = {}
grafo["E"] = {}
```

> **IMPOSTIAMO I LINK**
* Adesso andremo a creare i link tra i vari nodi come da immagine:
```python
grafo["nodo_partenza"]["nodo_arrivo"] = peso
# Link S -> A e S -> C
grafo["S"]["A"] = 2
grafo["S"]["C"] = 4

# Link A -> B e A -> D
grafo["A"]["B"] = 10
grafo["A"]["D"] = 9

# Link B -> E
grafo["B"]["E"] = 5

# Link C -> A e C -> D
grafo["C"]["A"] = 1
grafo["C"]["D"] = 7

# Link D -> E
grafo["D"]["E"] = 5

# Il link di destinazione va lasciato vuoto.
grafo["E"] = {}
```

> **IMPOSTAZIONE COSTO DEI NODI**
* Adesso dobbiamo creare un dizionario che tenga conto del peso di ogni singolo nodo
    * I nodi direttamente collegati al nodo di partenza avranno in automatico il peso del link.
    * I nodi non direttamente collegati al nodo di partenza avranno come valore temporaneo: infinito.
    * **IN QUESTO DIZIONARIO NON VA INDICATO IL NODO DI PARTENZA**

* si consigli di usare `math.inf` per il valore infinito utilizzabile importando il modulo *math* con: `import math`.

* Creiamo il dizionario:
```python
costoNodi = {}
```
* Settiamo il dizionario:
```python
costoNodi["nodo"] = peso

costoNodi["A"] = 2
costoNodi["B"] = 4
costoNodi["C"] = math.inf
costoNodi["D"] = math.inf
costoNodi["E"] = math.inf
```

> **CREAZIONE TABELLA DEI 'PARENTI'**
* Il dizionario che andiamo a creare adesso, serve per tenere traccia del percorso minimo da seguire prodotto dall'algoritmo.
    * Se il nodo non è direttamente collegato al nodo di partenza impostare come valore `None`.
    * È più semplice spiegare direttamente il codice. :happy:
    * **IN QUESTO DIZIONARIO NON VA INDICATO IL NODO DI PARTENZA**
    
* Creiamo il dizionario:
```python
parents = {}
```

* Settiamo il dizionario:
```python
# Se il nodo è direttamente collegato al nodo di partenza:
parents["nodo"] = "nodo_di_partenza"

# Se il nodo NON è direttamente collegato al nodo di partenza:
parents["nodo"] = None

# Quindi:
parents["A"] = "start"
parents["B"] = "start"
parents["C"] = None
parents["D"] = None
parents["E"] = None
```

> **TABELLA DEI NODI PROCESSATI**
* Serve al prigramma per ricordare quali nodi ha già elaborato ed evitare che entri in loop.
```python
processati = []
```

### ULTIME COSE
* Adesso abbiamo finito, se tutto è adato bene il risualtato del programma dovrebbe essere questo:
```
Percorso:  S -> A -> D -> E
```
![grafoResult](/img/grafoResult.png)

### ESEMPI
* **Se vuoi vedere degli esempi, li puoi trovare dentro i file chiamati: `grafoN.py`.**
* **Per provarli non ti basta che copiare il codice al loro interno ed inserirlo nel file `Dijkstra.py` nell'apposita sezione.**


### RINGRAZIAMENTI

* **Sempre i notri poveri neuroni.**
* **La guida al markdown** - [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

