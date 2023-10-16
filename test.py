import enhanced_traversals
from graph import *


def main() -> None:
    graph = build_test_graph()
    print('Testing DFS2 from 0 to 4')
    test_DFS2(graph, 0, 4)
    print('Testing BFS2 from 0 to 5')
    test_BFS2(graph, 0, 5, 3)
    print('Testing DFS3 from 5')
    test_DFS3(graph, 5, 5)
    print('Testing BFS3 from 2')
    test_BFS3(graph, 2, 5, 5, 2)
    print('Testing if graph is connected')
    test_is_connected(graph, True)
    print('Testing if graph has cycle')
    test_has_cycle(graph, True)
    print('Testing random graph creation')
    test_create_random_graph(10, 200, 5)


def build_test_graph() -> Graph:
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 5)
    return g


def test_DFS2(g: Graph, node1: int, node2: int) -> None:
    path = enhanced_traversals.DFS2(g, node1, node2)
    print(path)
    assert path[0] == node1
    assert path[-1] == node2
    for n1, n2 in zip(path, path[1:]):
        assert g.are_connected(n1, n2)


def test_BFS2(g: Graph, node1: int, node2: int, expected: int) -> None:
    path = enhanced_traversals.BFS2(g, node1, node2)
    print(path)
    assert path[0] == node1
    assert path[-1] == node2
    for n1, n2 in zip(path, path[1:]):
        assert g.are_connected(n1, n2)
    assert len(path) == expected + 1


def test_DFS3(g: Graph, node1: int, expected: int) -> None:
    predecessors = enhanced_traversals.DFS3(g, node1)
    print(predecessors)
    assert len(predecessors) == expected


def test_BFS3(g: Graph, node1: int, node2: int, expected_size: int, expected_dist: int) -> None:
    predecessors = enhanced_traversals.BFS3(g, node1)
    print(predecessors)
    assert len(predecessors) == expected_size
    path = enhanced_traversals.reconstruct_path(node1, node2, predecessors)
    print(path)
    assert len(path) == expected_dist + 1


def test_is_connected(g: Graph, expected: bool) -> None:
    assert enhanced_traversals.is_connected(g) == expected


def test_has_cycle(g: Graph, expected: bool) -> None:
    assert enhanced_traversals.has_cycle(g) == expected


def test_create_random_graph(min_nodes: int, max_nodes: int, min_edges: int):
    for _ in range(100):
        num_nodes = random.randint(min_nodes, max_nodes)
        max_edges = (num_nodes ** 2 - num_nodes) // 2
        num_edges = random.randint(min_edges, num_nodes ** 2)
        total_edges = min(max_edges, num_edges)
        edge_count = 0
        g = create_random_graph(num_nodes, num_edges)
        assert g.number_of_nodes() == num_nodes
        for n in range(g.number_of_nodes() - 1):
            edge_count += sum(1 for node in g.adjacent_nodes(n) if node > n)

        assert edge_count == total_edges

    print('Graph created successfully')


if __name__ == '__main__':
    main()
