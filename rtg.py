import random
import itertools
import collections
import numpy as np
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

def weighted_choice_fac(choices, ps):
    """
    weighted choice factory
    I could also have futzed with decorator but this is easier
    """
    total = 0
    cum_ps = []
    for p in ps:
        total += p
        cum_ps.append(total)
    def weighted_choice():
        x = random.random() * total
        return choices[bisect.bisect(cum_ps, x)]
    return weighted_choice


def iu_gen_word(weighted_choice_fn, p):
    word = ""
    word = word + weighted_choice_fn() + ","
    while random.random() > p:
        word = word + weighted_choice_fn() + ","
    return word

def adjust_matrix_homophily(mat, beta):
    #assumes a square matrix
    #also assumes 0 < beta < 1
    mat_shape = mat.shape
    print mat_shape
    for x in xrange(mat_shape[0]):
        row_sum = 0
        for y in xrange(mat_shape[1]):
            if x != y:
                temp = mat[x, y] * beta
                row_sum += mat[x,y] - (temp)
                mat[x, y] = temp
        mat[x,x] += row_sum
    return mat

def rtg_iu(k, qs, p, W):
    k_set = map(str, range(k))
    weighted_choice_fn = weighted_choice_fac(k_set, qs)
    words = [iu_gen_word(weighted_choice_fn, p) for word in xrange(W)]
    return words


def create_qmat(qs, p):
    qs.append(p)
    qs = np.array(qs)
    qs = np.atleast_2d(qs / sum(qs))
    qmat = qs * qs.T
    return qmat, qs.shape[0]-1

def q_gen(k_set, qmat_cum):
    """
    Corresponds to SelectNodeLabels in the RTG paper
    qmat_cum is a cumulative sum thing
    """
    l1, l2 = "", ""
    l1_term, l2_term = False, False
    while ((not l1_term) or (not l2_term)):
        rand = random.random() #only one random number because
        #we're selecting from ravelled matrix
    return l1, l2

def rtg(k, qs, p, W, beta):
    k_set = map(str, range(k))
    qmat, len_qmat = create_qmat(qs, p)
    qmat = adjust_matrix_homophily(qmat, beta)
    qmat_cum = np.cumsum(qmat.ravel())
    print qmat_cum
    pass

if __name__ == "__main__":
    words = rtg(10, range(2,12), 0.5, 1000, 0.9)
    #print words_to_graph(words)
