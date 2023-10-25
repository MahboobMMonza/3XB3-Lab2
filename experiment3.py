from approximations import *
from utilities import *


def run_experiment3a():
    num_nodes = 8
    edge_ranges = range(1, 31, 4)
    num_graphs = 1000

    x_vals = []
    approx1_vals, approx2_vals, approx3_vals = [], [], []

    for num_edges in edge_ranges:
        approx1_total = 0
        approx2_total = 0
        approx3_total = 0
        min_vc_size_total = 0

        for _ in range(num_graphs):
            graph = create_random_graph(num_nodes, num_edges)
            x_vals.append(min(num_edges, (num_nodes ** 2 - num_nodes) // 2))

            min_vc_size = len(MVC(graph))
            min_vc_size_total += min_vc_size

            approx1_vc_size = len(approx1(graph))
            approx1_total += approx1_vc_size

            approx2_vc_size = len(approx2(graph))
            approx2_total += approx2_vc_size

            approx3_vc_size = len(approx3(graph))
            approx3_total += approx3_vc_size

        proportion_avg_vc_approx1 = min_vc_size_total / approx1_total
        proportion_avg_vc_approx2 = min_vc_size_total / approx2_total
        proportion_avg_vc_approx3 = min_vc_size_total / approx3_total

        approx1_vals.append(proportion_avg_vc_approx1 * 100)
        approx2_vals.append(proportion_avg_vc_approx2 * 100)
        approx3_vals.append(proportion_avg_vc_approx3 * 100)

    create_plot(x_vals,
                [approx1_vals, approx2_vals, approx3_vals],
                legend_labels=["Approximation 1", "Approximation 2", "Approximation 3"],
                title="Expected Performance of MVC Approximations",
                description="Performance relative to true MVC size, repeated for 1000 graphs and nodes = 8",
                x_label="Number of Edges",
                y_label="Expected Performance (%)")


def run_experiment3b():
    num_nodes = 8
    edge_ranges = range(1, 31, 4)
    num_graphs = 1000
    x_vals = []

    approx1_matches = []
    approx2_matches = []
    approx3_matches = []

    for num_edges in edge_ranges:
        matches_approx1 = 0
        matches_approx2 = 0
        matches_approx3 = 0
        x_vals.append(min(num_edges, (num_nodes ** 2 - num_nodes) // 2))

        for _ in range(num_graphs):
            graph = create_random_graph(num_nodes, num_edges)

            min_vc_size = len(MVC(graph))

            approx1_vc_size = len(approx1(graph))
            approx2_vc_size = len(approx2(graph))
            approx3_vc_size = len(approx3(graph))

            if min_vc_size == approx1_vc_size:
                matches_approx1 += 1
            if min_vc_size == approx2_vc_size:
                matches_approx2 += 1
            if min_vc_size == approx3_vc_size:
                matches_approx3 += 1

        total_graphs = num_graphs
        approx1_percent = (matches_approx1 / total_graphs) * 100
        approx2_percent = (matches_approx2 / total_graphs) * 100
        approx3_percent = (matches_approx3 / total_graphs) * 100

        approx1_matches.append(approx1_percent)
        approx2_matches.append(approx2_percent)
        approx3_matches.append(approx3_percent)

    create_plot(list(edge_ranges),
                [approx1_matches, approx2_matches, approx3_matches],
                legend_labels=["Approximation 1", "Approximation 2", "Approximation 3"],
                title="Accuracy of Approximations in Obtaining MVC Result ",
                description="Repeated for 1000 graphs given nodes = 8 and edges ranging from 1-30",
                x_label="Number of Edges",
                y_label="Accuracy of Approximation(%)")


def run_experiment3c():
    node_ranges = range(5, 16, 1)
    num_graphs = 1000

    approx1_matches = []
    approx2_matches = []
    approx3_matches = []

    for num_nodes in node_ranges:
        matches_approx1 = 0
        matches_approx2 = 0
        matches_approx3 = 0
        num_edges = 2 * num_nodes

        for _ in range(num_graphs):
            graph = create_random_graph(num_nodes, num_edges)

            min_vc_size = len(MVC(graph))

            approx1_vc_size = len(approx1(graph))
            approx2_vc_size = len(approx2(graph))
            approx3_vc_size = len(approx3(graph))

            if min_vc_size == approx1_vc_size:
                matches_approx1 += 1
            if min_vc_size == approx2_vc_size:
                matches_approx2 += 1
            if min_vc_size == approx3_vc_size:
                matches_approx3 += 1

        total_graphs = num_graphs
        approx1_percent = (matches_approx1 / total_graphs) * 100
        approx2_percent = (matches_approx2 / total_graphs) * 100
        approx3_percent = (matches_approx3 / total_graphs) * 100

        approx1_matches.append(approx1_percent)
        approx2_matches.append(approx2_percent)
        approx3_matches.append(approx3_percent)

    create_plot(list(node_ranges),
                [approx1_matches, approx2_matches, approx3_matches],
                legend_labels=["Approximation 1", "Approximation 2", "Approximation 3"],
                title="Accuracy of Approximations in Obtaining MVC Result",
                description="Repeated for 1000 graphs given edges = 2 * nodes and nodes ranging from 5-15",
                x_label="Number of Nodes",
                y_label="Accuracy of Approximation (%)")


def main():
    run_experiment3a()
    run_experiment3b()
    run_experiment3c()


if __name__ == '__main__':
    main()
