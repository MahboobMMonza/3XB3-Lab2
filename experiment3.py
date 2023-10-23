from utilities import *
from approximations import *


def run_experiment3a():
    num_nodes = 8
    edge_ranges = range(1, 31, 4)
    num_graphs = 1000

    x_vals = list(edge_ranges)
    approx1_vals, approx2_vals, approx3_vals = [], [], []

    for num_edges in edge_ranges:
        approx1_total = 0
        approx2_total = 0
        approx3_total = 0
        min_vc_size_total = 0

        for _ in range(num_graphs):
            graph = create_random_graph(num_nodes, num_edges)

            min_vc_size = len(MVC(graph))
            min_vc_size_total += min_vc_size

            approx1_vc_size = len(approx1(graph))
            approx1_total += approx1_vc_size

            approx2_vc_size = len(approx2(graph))
            approx2_total += approx2_vc_size

            approx3_vc_size = len(approx3(graph))
            approx3_total += approx3_vc_size

        avg_min_vc_size = min_vc_size_total / num_graphs
        avg_vc_approx1 = approx1_total / num_graphs
        avg_vc_approx2 = approx2_total / num_graphs
        avg_vc_approx3 = approx3_total / num_graphs

        approx1_vals.append(avg_min_vc_size / avg_vc_approx1 * 100)
        approx2_vals.append(avg_min_vc_size / avg_vc_approx2 * 100)
        approx3_vals.append(avg_min_vc_size / avg_vc_approx3 * 100)

    create_plot(
        x_vals,
        [approx1_vals, approx2_vals, approx3_vals],
        legend_labels=["Approximation 1", "Approximation 2", "Approximation 3"],
        title="Proportion of True MVC Sizes to Approximation Size",
        description="Performance relative to minimum vertex cover size",
        x_label="Number of Edges",
        y_label="Performance (%)"
    )


def main():
    run_experiment3a()


if __name__ == '__main__':
    main()