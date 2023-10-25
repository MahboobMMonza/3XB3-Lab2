from graph import Graph


def make_MIS_combo(g: Graph, comb: int) -> set[int]:
    mis = set()
    for node in range(g.number_of_nodes()):
        if comb & (1 << node):
            mis.add(node)

    return mis


def is_independent_set(g: Graph, ind_set: set[int]):
    for start in range(g.number_of_nodes()):
        for end in g.adjacent_nodes(start):
            if start in ind_set and end in ind_set:
                return False

    return True


def MIS(g: Graph) -> set[int]:
    combinations: list[int] = sorted([i for i in range(1 << g.number_of_nodes())], key=lambda a: -a.bit_count())
    max_mis: set[int] = set()
    for combo in combinations:
        max_mis = make_MIS_combo(g, combo)
        if is_independent_set(g, max_mis):
            break

    return max_mis
