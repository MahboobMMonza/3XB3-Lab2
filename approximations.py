import random

from graph import Graph
from vertex_covers import *


def approx1(g: Graph) -> set[int]:
    adj = {i: set() for i in range(g.number_of_nodes())}
    cover, included_neighbours = set(), set()
    # Create a local "copy" of the adj list to update
    for i in range(g.number_of_nodes()):
        for node in g.adjacent_nodes(i):
            adj[i].add(node)

    while not is_vertex_cover(g, cover):
        max_degree, highest = -1, -1
        for node in range(g.number_of_nodes()):
            if node in cover:
                continue
            # Update the max number and node with the highest degree
            if len(adj[node]) > max_degree:
                max_degree = len(adj[node])
                highest = node

        # Add the highest degree node to the list
        cover.add(highest)
        # Remove all edges connected to the highest degree node
        for i in range(g.number_of_nodes()):
            if i == highest:
                adj[i] = set()
            else:
                adj[i].discard(highest)

    return cover


def approx2(g: Graph) -> set[int]:
    cover = set()
    vertices = {i for i in range(g.number_of_nodes())}
    while not is_vertex_cover(g, cover):
        v = random.choice(tuple(vertices))
        vertices.discard(v)
        cover.add(v)

    return cover


def approx3(g: Graph) -> set[int]:
    cover = set()
    edges = set()
    for i in range(g.number_of_nodes()):
        for node in g.adjacent_nodes(i):
            edges.add((min(i, node), max(i, node)))

    while not is_vertex_cover(g, cover):
        edge = random.choice(tuple(edges))
        edges.discard(edge)
        cover.add(edge[0])
        cover.add(edge[1])
        edges = {e for e in edges if not edge[0] in e and not edge[1] in e}

    return cover