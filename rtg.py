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
    qs_norm = np.atleast_2d(np.array(qs) / np.linalg.norm(np.array(qs)))
    len_qmat = qs_norm.shape[1] - 1 #the index of qmat that indicates space
    q_mat = qs_norm * qs_norm.T #maybe un-normalized now? I don't know
    return q_mat

def q_gen(k_set, qmat):
    """
    Corresponds to SelectNodeLabels in the RTG paper
    I think he was supposed
    """
    l1, l2 = "", ""
    l1_term, l2_term = False, False
    while ((not l1_term) and (not l2_term)):
        rand1 = random.random()
        rand2 = random.random()
        #stuff stuff stuff
    return l1, l2

def rtg(k, qs, p, W, beta):
    k_set = map(str, range(k))
    qmat = create_qmat(qs, p)
    qmat = adjust_matrix_homophily(qmat, beta)
    pass

if __name__ == "__main__":
    words = rtg(10, range(2,12), 0.5, 1000, 0.9)
    #print words_to_graph(words)
