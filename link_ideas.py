import networkx as nx
import random

def rtg_ie(num_words = 10, k=10, q=0.1):
    """
    RTG with Independent Equiprobable Keys
    @param num_words: number of words the monkey should type
    @param k: int, range of possible characters
    @parma q: float, probability of monkey hitting spacebar
    """
    def monkey_type(k, q):
        if random.random() < q:
            return 0
        else:
            return random.choice(xrange(1,k+1))
    words = []
    for x in xrange(num_words):
        curr_char = -1
        curr_word = []
        while curr_char != 0:
            curr_char = monkey_type(k,q)
            curr_word.append(curr_char)
        curr_word = curr_word[:-1]
        words.append(",".join(map(str, curr_word)))
    return words

if __name__ == "__main__":
    rtg_ie()
