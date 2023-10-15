from enhanced_traversals import has_cycle
from utilities import *


def run_experiment1() -> None:
    # Next step is to create run across different numbers of nodes
    num_nodes = [101, 501, 1001, 2001, 4001]
    benchmarks, reps, include_start = 20, 30, False
    legend_labels = [f'{nodes} Node Graph' for nodes in num_nodes]
    title = 'Proportion of Edges vs Cycle Probability'
    desc = (f'{benchmarks + include_start} benchmarks up to (n - 1) edges for n nodes with {reps} repetitions'
            f' per edge count')
    x_label = 'Proportion of Edges (up to maximum of n - 1 edges)'
    y_label = 'Probability of a Cycle'
    results = [(prp, prob) for prp, prob in incrementing_node_graph_evals(num_nodes,
                                                                          lambda n: 0 * n,
                                                                          lambda n: n - 1,
                                                                          benchmarks,
                                                                          reps,
                                                                          include_start,
                                                                          has_cycle)]
    proportion = results[0][0]
    probability = [res[1] for res in results]
    create_plot(proportion, probability, legend_labels, title, desc, x_label, y_label, 1.60)


if __name__ == '__main__':
    run_experiment1()
