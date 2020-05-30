def order(sentence):
  if sentence == "":
      return sentence
  wordsplit = sentence.split(' ')
  print(wordsplit)
  length = len(wordsplit)
  arr = [None]*length
  if length > 0:      
      for word in wordsplit:
          str = (list(word))
          str.sort()
          n = int(str[0])
          arr[n-1] = word
      ans = ' '.join(x for x in arr)
      print(ans)
      return ans