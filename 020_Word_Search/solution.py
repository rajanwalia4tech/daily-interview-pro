def word_search(matrix, word):
    wordLen = len(matrix[0])

    for i, _ in enumerate(matrix):
        word_ = ''.join(matrix[i])
        if word_:
            if word in word_:
                return True

    for i in range(wordLen):
        temp = []
        for j in matrix:
            temp.append(j[i])
        word_ = ''.join(temp)
        if word_:
            if word in word_:
                return True
    return False

  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]
print word_search(matrix, 'FOAM')
# True