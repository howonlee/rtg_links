import string
import random

def ie_gen_word(k_set, p):
    word = ""
    word = word + random.choice(k_set) + ","
    while random.random() > p:
        word = word + random.choice(k_set) + ","
    return word

def rtg_ie(k, p, W):
    k_set = map(str, range(k))
    words = [gen_word(k_set, p) for word in xrange(W)]
    return words

def iu_gen_word(k_set, qs, p):
    pass

def rtg_iu(k, p):
    pass

def rtg(k, q, w, beta):
    pass

if __name__ == "__main__":
    print rtg_ie(5, 0.15, 1000)
