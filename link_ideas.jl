using Distributions

function ie_monkey_type(k, q)
  if rand() < q
    return 0
  else
    return rand.choice(xrange(k))
  end
end

function iu_monkey_type(k, q, ps)
  ##
end

function write_rtg_ie(num_words=1000, k=5, q=0.1)
  #RTG with Independent Equiprobable Keys
  #@param num_words: number of words the monkey should type
  #@param k: int, range of possible characters
  #@param q: float, probability of monkey hitting spacebar
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
end

function write_rtg_iu(num_words=1000, k=5, q=0.1, ps=[0.03,0.05,0.1,0.22,0.3])
  ##
end

println(write_rtg_ie())
