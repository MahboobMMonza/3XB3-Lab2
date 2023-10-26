# Undirected graph using an adjacency list
import random


class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = set()

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = set()

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].add(node2)
            self.adj[node2].add(node1)

    def number_of_nodes(self):
        return len(self.adj)


def create_random_graph(num_nodes: int, num_edges: int) -> Graph:
    # You can't have a graph with a non-positive number of nodes/edges
    num_nodes, num_edges = max(num_nodes, 1), max(num_edges, 0)
    # And undirected graphs can have a maximum of (n * (n - 1)) / 2 edges
    num_edges = min(num_edges, (num_nodes ** 2 - num_nodes) // 2)
    g = Graph(num_nodes)
    # Use a set to track all the edges added so far
    existing_edges = set()
    potential_neighbours = {i: set() for i in range(g.number_of_nodes() - 1)}
    for i in range(g.number_of_nodes() - 1):
        for j in range(i + 1, g.number_of_nodes()):
            potential_neighbours[i].add(j)

    while len(existing_edges) < num_edges:
        # In an undirected graph, an edge (u, v) can always be represented such that u < v. So we only need to
        # track that the randomly generated numbers are not equal (no self-loops), and then we can swap values
        # if the generated v is less than the generated u. Then we can check if this edge has already been
        # created, and act accordingly. The `are_connected` function could be used, but since adjacency is done
        # using a Python list, that is an O(n) operation. That could be fixed by using a set for adjacency
        # instead (granted the adding operation itself is O(n)).
        u = random.choice(tuple(potential_neighbours.keys()))
        v = random.choice(tuple(potential_neighbours[u]))
        g.add_edge(u, v)
        existing_edges.add((u, v))
        potential_neighbours[u].discard(v)
        if len(potential_neighbours[u]) == 0:
            del potential_neighbours[u]

    return g
