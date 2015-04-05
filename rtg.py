import random
import itertools
import collections
import networkx as nx
import bisect

"""
Util functions
"""
def grouper(iterable, n):
    """
    Collect data into fixed-length chunks or blocks
    """
    args = [iter(iterable)] * n
    return zip(*args)

def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect.bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -1)

def words_to_graph(words):
    wtg_order = sorted(list(set(words)))
    word_idx = 0
    words_grouped = grouper(words, 2)
    graph = []
    for first, second in words_grouped:
        graph.append((binary_search(wtg_order, first), binary_search(wtg_order, second)))
    return graph


def ie_gen_word(k_set, p):
    word = ""
    word = word + random.choice(k_set) + ","
    while random.random() > p:
        word = word + random.choice(k_set) + ","
    return word

def rtg_ie(k, p, W):
    k_set = map(str, range(k))
    words = [ie_gen_word(k_set, p) for word in xrange(W)]
    return words


def iu_gen_word(k_set, qs, p):
    pass

def rtg_iu(k, p):
    pass

def rtg(k, q, w, beta):
    pass

if __name__ == "__main__":
    words = rtg_ie(5, 0.15, 1000)
    words_to_graph(words)
