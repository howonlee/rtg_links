
function ie_monkey_type(k, q)
  if rand() < q
    return 0
  else
    return rand.choice(xrange(k))
  end
end

function write_rtg_ie(num_words=1000, k=10, q=0.1)
  #=
  RTG with Independent Equiprobable Keys
  @param num_words: number of words the monkey should type
    @param k: int, range of possible characters
    @param q: float, probability of monkey hitting spacebar
    =#
    words = some array or other
    for x in xrange(num_words):
      curr_char = -1
      curr_word = []
      while curr_char != 0:
        curr_char = monkey_type(k,q)
        curr_word.append(curr_char)
      end
      curr_word = curr_word[:-1]
      words.append(",".join(map(str, curr_word)))
    end
    words
    return words
  end
