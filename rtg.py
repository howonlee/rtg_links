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
    k_len = len(k_set)
    while ((not l1_term) or (not l2_term)): #I may regret this one
        rand = random.random() #only one random number because
        idx = np.searchsorted(qmat_cum, rand)
        i, j = idx // (k_len + 1), idx % (k_len + 1)
        if i < k_len and j < k_len:
            if not l1_term:
                l1 = l1 + k_set[i] + ","
            if not l2_term:
                l2 = l2 + k_set[j] + ","
        elif i < k_len and j == k_len:
            if not l1_term:
                l1 = l1 + k_set[i] + ","
            l2_term = True
        elif i == k_len and j < k_len:
            if not l2_term:
                l2 = l2 + k_set[j] + ","
            l1_term = True
        else:
            l1_term = True
            l2_term = True
    return l1, l2

def rtg(k, qs, p, W, beta):
    k_set = map(str, range(k))
    qmat, len_qmat = create_qmat(qs, p)
    qmat = adjust_matrix_homophily(qmat, beta)
    qmat_cum = np.cumsum(qmat.ravel())
    return [q_gen(k_set, qmat_cum) for word in xrange(W)]

if __name__ == "__main__":
    words = rtg(5, [0.03,0.05,0.1,0.22,0.3], 0.16, 1000000, 0.4)
    words = [single_word for tup in words for single_word in tup]
    with open("rtg_corpus.txt", "w") as rtg_file:
        rtg_file.write(" ".join(words))
    #gen_net = words_to_graph(words)
    #for first, second in gen_net:
    #    print "%s %s" % (first, second)
