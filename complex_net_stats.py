import snap
import networkx as nx
import matplotlib.pyplot as plt
import operator
import collections
import sys

def load(fname="turb.edgelist"):
    return snap.LoadEdgeList(snap.PUNGraph, fname, 0, 1)

def plot_degrees(fname="turb.edgelist", pref="turb"):
    with open(fname, "r") as net_file:
        net = nx.read_edgelist(net_file)
        degree_sequence=sorted(nx.degree(net).values(),reverse=True)
        plt.clf()
        plt.cla()
        plt.loglog(degree_sequence, 'b-')
        plt.title("Degree Counts")
        plt.xlabel("Degree")
        plt.ylabel("Count")
        plt.savefig(pref + "_degree_plot")

def triads(net, pref):
    TriadCntV = snap.TIntPrV()
    Cf = snap.GetTriadParticip(net, TriadCntV)
    pairs = []
    for pair in TriadCntV:
        pairs.append((pair.GetVal1(), pair.GetVal2()))
    tris = map(operator.itemgetter(0), pairs)
    nodes = map(operator.itemgetter(1), pairs)
    plt.clf()
    plt.cla()
    plt.loglog(tris, nodes, 'b-')
    plt.title("Triangle Participation")
    plt.xlabel("Participation")
    plt.ylabel("Count")
    plt.savefig(pref + "_triads")

def clustering_coeffs(net, pref="turb"):
    DegToCCfV = snap.TFltPrV()
    Cf = snap.GetClustCf(net, DegToCCfV, -1)
    pairs = []
    for pair in DegToCCfV:
        pairs.append((pair.GetVal1(), pair.GetVal2()))
    degs = map(operator.itemgetter(0), pairs)
    coeffs = map(operator.itemgetter(1), pairs)
    plt.clf()
    plt.cla()
    plt.loglog(degs, coeffs, 'b-')
    plt.title("Clustering Coefficients")
    plt.xlabel("Degree")
    plt.ylabel("Coefficient")
    plt.savefig(pref + "_clustering_coeff")

def singular_values(net, pref="turb"):
    EigVals = 30
    PEigV = snap.TFltV()
    snap.GetEigVals(net, EigVals, PEigV)
    eig_arr = []
    for item in PEigV:
        eig_arr.append(item)
    plt.clf()
    plt.cla()
    plt.loglog(eig_arr, 'b-')
    plt.xlabel("rank")
    plt.ylabel("eigenvalues")
    plt.title("Eigenvalues")
    plt.savefig(pref + "_eigvals")

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print "usage: stats.py edge_file_name plot_prefix"
        sys.exit(0)
    net = load(sys.argv[1])
    plot_degrees(sys.argv[1], sys.argv[2])
    triads(net, sys.argv[2])
    clustering_coeffs(net, sys.argv[2])
    singular_values(net, sys.argv[2])
