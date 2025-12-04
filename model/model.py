import networkx as nx
from database.dao import DAO
from model.rifugio import Rifugio
from collections import deque


class Model:
    def __init__(self):
        self.G = nx.Graph()

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """

        # Pulisco il grafo
        self.G.clear()
        # Prendo dal database tutte le connessioni <= all'anno
        connessioni = DAO.rifugi_per_anno(year)
        for c in connessioni:
            # Creo due oggetti Rifugio corrispondenti ai due estremi del sentiero
            r1 = Rifugio(c["id_rifugio1"], c["nome1"], c["localita1"])
            r2 = Rifugio(c["id_rifugio2"], c["nome2"], c["localita2"])
            # Aggiungo i nodi al grafo
            self.G.add_node(r1)
            self.G.add_node(r2)
            # Aggiungo un arco
            self.G.add_edge(r1, r2)




    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """

        return list(self.G.nodes)

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """

        return len(list(self.G.neighbors(node)))

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """

        return nx.number_connected_components(self.G)

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """


        a = self._get_reachable_bfs_tree(start)
        b = self._get_reachable_iterative(start)
        return a
    def _get_reachable_bfs_tree(self, start):
        # Creo l'albero a partire dal nodo di partenza
        tree = nx.bfs_tree(self.G, start)
        # Estraggo tutti i nodi raggiunti
        nodes = list(tree.nodes())
        # Rimuovo il nodo di partenza
        nodes.remove(start)
        return nodes


    def _get_reachable_iterative(self, start):
        # Uso un insieme per memorizzare i nodi già visitati
        visited = set()
        # Uso deque
        queue = deque([start])
        while queue:
            # Estraggo il nodo più vecchio in queue
            current = queue.popleft()
            # controllo i vicini del nodo corrente
            for n in self.G.neighbors(current):
                # controllo che il nodo corrente non sia il nodo di partenza e che
                # non lo abbia già visitato
                if n not in visited and n != start:
                    visited.add(n)
                    queue.append(n)
        return list(visited)