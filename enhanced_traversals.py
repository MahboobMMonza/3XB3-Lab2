from collections import deque

from graph import Graph


def BFS2(g: Graph, node1: int, node2: int) -> list[int]:
    predecessor, q, visited = {}, deque([node1]), {node1: True}
    for node in range(g.number_of_nodes()):
        visited[node] = node == node1

    while q and not visited[node2]:
        cur_node = q.popleft()
        for node in g.adjacent_nodes(cur_node):
            if not visited[node]:
                predecessor[node] = cur_node
                visited[node] = True
                if node == node2:
                    break
                q.append(node)

    return reconstruct_path(node1, node2, predecessor)


def BFS3(g: Graph, node1: int) -> dict[int, int]:
    predecessor, q, visited = {}, deque([node1]), {node1: True}
    for node in range(g.number_of_nodes()):
        visited[node] = node == node1

    while q:
        cur_node = q.popleft()
        for node in g.adjacent_nodes(cur_node):
            if not visited[node]:
                predecessor[node] = cur_node
                visited[node] = True
                q.append(node)

    return predecessor


def reconstruct_path(node1: int, node2: int, predecessor: dict[int, int]) -> list[int]:
    path, cur_node = [], node2
    path.append(cur_node)
    while cur_node != node1:
        cur_node = predecessor.get(cur_node, -1)
        if cur_node == -1:
            return []
        path.append(cur_node)

    path.reverse()
    return path


def DFS2(g: Graph, node1: int, node2: int) -> list[int]:
    predecessor, s, visited = {}, [node1], {node1: True}
    for node in range(g.number_of_nodes()):
        visited[node] = False

    while s and not visited[node2]:
        cur_node = s.pop()
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        # Reversing the list has no effect on actual DFS except
        # that the first node is visited first and the last node
        # is visited last
        for node in reversed(g.adjacent_nodes(cur_node)):
            if visited[node]:
                continue
            predecessor[node] = cur_node
            if node == node2:
                visited[node] = True
                break
            s.append(node)

    return reconstruct_path(node1, node2, predecessor)


def DFS3(g: Graph, node1: int) -> dict[int, int]:
    predecessor, s, visited = {}, [node1], {node1: True}
    for node in range(g.number_of_nodes()):
        visited[node] = False

    while s:
        cur_node = s.pop()
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        # Reversing the list has no effect on actual DFS except
        # that the first node is visited first and the last node
        # is visited last
        for node in reversed(g.adjacent_nodes(cur_node)):
            if visited[node]:
                continue
            predecessor[node] = cur_node
            s.append(node)

    return predecessor


def is_connected(graph: Graph) -> bool:
    # Since the graph is undirected, a connected graph is possible if, from
    # a single source node, the remaining nodes are reachable. This observation
    # holds because if traversing C <=> A is possible, and traversing C <=> B is
    # possible, then traversing A <=> B is possible by at least traversing
    # A <=> C <=> B. Hence, if one node can reach all other nodes, then each node
    # can reach every other node.
    return len(DFS3(graph, 0)) == graph.number_of_nodes() - 1


def has_cycle(graph: Graph) -> bool:
    # Use the gist of DFS, but to maintain non-recursion (we hate recursion here),
    # we will just check that the visited neighbour is not the one that added the
    # current node to the stack, by adding a second value to each stack element which
    # represents the immediate predecessor. Since a graph can be cyclic but not connected,
    # we will need to search all remaining unvisited nodes until we either find a cycle
    # or no nodes remain.
    #
    # Credit to https://stackoverflow.com/questions/31532887/detecting-cycle-in-an-undirected-graph-using-iterative-dfs
    visited, s = {}, []
    for node in range(graph.number_of_nodes()):
        visited[node] = False

    # Complexity is still O(V + E) since each node is relaxed at most once
    for source_node in range(graph.number_of_nodes()):
        if visited[source_node]:
            continue
        s.append((source_node, -1))
        visited[source_node] = True
        # Modified version of DFS that "marks" the node at discovery
        while s:
            cur_node, pred = s.pop()
            for node in reversed(graph.adjacent_nodes(cur_node)):
                # If the node has been visited before and is not the caller, return true
                # otherwise skip if it's the caller
                if visited[node] and node != pred:
                    return True
                elif node == pred:
                    continue
                s.append((node, cur_node))
                visited[node] = True

    return False
