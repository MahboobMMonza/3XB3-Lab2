from enhanced_traversals import is_connected
from utilities import *


def run_experiment2a() -> None:
    num_nodes = [26, 77]
    benchmarks, reps, include_start = 20, 40, True
    legend_labels = [f'{nodes} Node Graph' for nodes in num_nodes]
    title = 'Proportion of Edges vs Connectivity Probability'
    desc = (f'{benchmarks + include_start} benchmarks from (n - 1) edges for n nodes with {reps} repetitions'
            f' per edge count, proportional to total possible edges in the graph')
    x_label = 'Proportion of Edges (from minimum number edges needed for connectivity)'
    y_label = 'Probability of Graph Connectivity'
    results = [(prp, prob) for prp, prob in incrementing_node_graph_evals(num_nodes,
                                                                          lambda n: n - 1,
                                                                          lambda n: ((n ** 2 - n) // 2 - (
                                                                              n - 1)) // 5 * 2 + (n - 1),
                                                                          benchmarks,
                                                                          reps,
                                                                          include_start,
                                                                          is_connected,
                                                                          true_max_eval=lambda n: (n ** 2 - n) // 2)]
    proportion = results[0][0]
    probability = [res[1] for res in results]
    create_plot(proportion, probability, legend_labels, title, desc, x_label, y_label, 1.60, False)


def run_experiment2b() -> None:
    num_nodes = [102, 202, 302]
    benchmarks, reps, include_start = 10, 40, True
    legend_labels = [f'{nodes} Node Graph' for nodes in num_nodes]
    title = 'Proportion of Edges vs Connectivity Probability'
    desc = (f'{benchmarks + include_start} benchmarks from (n - 1) edges for n nodes with {reps} repetitions'
            f' per edge count, proportional to total possible edges in the graph')
    x_label = 'Proportion of Edges (from minimum number edges needed for connectivity)'
    y_label = 'Probability of Graph Connectivity'
    results = [(prp, prob) for prp, prob in incrementing_node_graph_evals(num_nodes,
                                                                          lambda n: n - 1,
                                                                          lambda n: ((n ** 2 - n) // 2 - (
                                                                              n - 1)) // 5 + (n - 1),
                                                                          benchmarks,
                                                                          reps,
                                                                          include_start,
                                                                          is_connected,
                                                                          true_max_eval=lambda n: (n ** 2 - n) // 2)]
    proportion = results[0][0]
    probability = [res[1] for res in results]
    create_plot(proportion, probability, legend_labels, title, desc, x_label, y_label, 1.60, True)


def main():
    run_experiment2a()
    run_experiment2b()


if __name__ == '__main__':
    main()
