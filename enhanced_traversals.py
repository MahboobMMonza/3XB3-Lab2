from collections import deque

from graph import Graph


def BFS2(g: Graph, node1: int, node2: int) -> list[int]:
    predecessor, q, visited = {}, deque([node1]), {node1: True}
    for node in g.adj:
        visited[node] = node == node1

    while q and not visited[node2]:
        cur_node = q.popleft()
        for node in g.adj[cur_node]:
            if not visited[node]:
                predecessor[node] = cur_node
                visited[node] = True
                if node == node2:
                    break
                q.append(node)

    return reconstruct_path(node1, node2, predecessor)


def BFS3(g: Graph, node1: int) -> dict[int, int]:
    predecessor, q, visited = {}, deque([node1]), {node1: True}
    for node in g.adj:
        visited[node] = node == node1

    while q:
        cur_node = q.popleft()
        for node in g.adj[cur_node]:
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
    for node in g.adj:
        visited[node] = False

    while s and not visited[node2]:
        cur_node = s.pop()
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        # Reversing the list has no effect on actual DFS except
        # that the first node is visited first and the last node
        # is visited last
        for node in reversed(g.adj[cur_node]):
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
    for node in g.adj:
        visited[node] = False

    while s:
        cur_node = s.pop()
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        # Reversing the list has no effect on actual DFS except
        # that the first node is visited first and the last node
        # is visited last
        for node in reversed(g.adj[cur_node]):
            if visited[node]:
                continue
            predecessor[node] = cur_node
            s.append(node)

    return predecessor
