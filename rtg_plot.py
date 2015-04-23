import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sci_sp
import networkx as nx

def main():
    net = nx.read_edgelist("rtg.edgelist")
    net_plot = nx.to_scipy_sparse_matrix(net)
    plt.spy(net_plot, markersize=0.2)
    plt.savefig("rtg_sparsemat")

if __name__ == "__main__":
    main()
