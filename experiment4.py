from independent_set import MIS
from utilities import *
from vertex_covers import MVC


def experiment4():
    num_nodes = 8
    edge_ranges = range(1, 31, 4)
    num_graphs = 1000

    x_vals = []
    mvc_avg_size, mis_avg_size, sum_size = [], [], []

    for num_edges in edge_ranges:
        mvc_total, mis_total = 0, 0
        x_vals.append(min(num_edges, (num_nodes ** 2 - num_nodes) // 2))

        for _ in range(num_graphs):
            graph = create_random_graph(num_nodes, num_edges)
            mvc = MVC(graph)
            mis = MIS(graph)
            mvc_total += len(mvc)
            mis_total += len(mis)

        mvc_avg_size.append(mvc_total / num_graphs)
        mis_avg_size.append(mis_total / num_graphs)
        sum_size.append((mvc_total + mis_total) / num_graphs)

    create_plot(x_vals,
                [mvc_avg_size, mis_avg_size, sum_size],
                legend_labels=["Average MVC Size", "Average MIS Size", "Sum of Average MIS and MVC Sizes"],
                title="Average MVC and MIS Sizes",
                description=f"Repeated for {num_graphs} graphs, nodes = {num_nodes}, edges ranging from 1-28",
                x_label="Number of Edges",
                y_label="Size",
                scale=1)


def main():
    experiment4()


if __name__ == '__main__':
    main()
