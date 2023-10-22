import matplotlib.pyplot as plt

from graph import create_random_graph


def create_plot(x_vals: list,
                y_vals: list[list],
                legend_labels: list[str],
                title: str,
                description: str,
                x_label: str,
                y_label: str,
                scale: float = 1,
                show_ticks: bool = True) -> None:
    height, width = plt.figure().get_figheight(), plt.figure().get_figwidth()
    plt.figure(figsize=(scale * width, scale * height))
    for yv, legend in zip(y_vals, legend_labels):
        plt.plot(x_vals, yv, linewidth=2, label=legend, marker='o')

    plt.xlabel(x_label)
    if show_ticks:
        plt.xticks(x_vals)
    plt.ylabel(y_label)
    plt.suptitle(title, fontsize=14)
    plt.title(description, fontsize=10)
    plt.legend(fontsize=10)
    plt.show()


def incrementing_edge_graph_evals(num_nodes: int,
                                  min_edges: int,
                                  max_edges: int,
                                  true_max_edges: int,
                                  benchmarks: int,
                                  repetitions: int,
                                  include_start: bool,
                                  evaluation: callable) -> tuple[list[float], list[float]]:
    step = (max_edges - min_edges) // benchmarks
    start = min_edges if include_start else min_edges + step
    probability, proportion = [], []
    for num_edges in range(start, max_edges + 1, step):
        probability.append(
            sum(evaluation(create_random_graph(num_nodes, num_edges)) for _ in range(repetitions)) / repetitions
        )
        proportion.append((num_edges - min_edges) / (true_max_edges - min_edges))

    return proportion, probability


def incrementing_node_graph_evals(node_sizes: list[int],
                                  min_eval: callable,
                                  max_eval: callable,
                                  benchmarks: int,
                                  repetitions: int,
                                  include_start: bool,
                                  graph_eval: callable,
                                  true_max_eval: callable = None) -> tuple[list[float], list[float]]:
    for num_nodes in node_sizes:
        min_edges, max_edges = min_eval(num_nodes), max_eval(num_nodes)
        true_max_edges = true_max_eval(num_nodes) if true_max_eval else max_edges
        yield incrementing_edge_graph_evals(num_nodes,
                                            min_edges,
                                            max_edges,
                                            true_max_edges,
                                            benchmarks,
                                            repetitions,
                                            include_start,
                                            graph_eval)


def find_values() -> list[int]:
    results = []
    for n in range(1, 3000):  # Iterate through a range of n values
        eval_eqn = ((n ** 2 - n) // 2 - (n - 1)) * 0.01
        if eval_eqn.is_integer():
            results.append(n)

    return results
