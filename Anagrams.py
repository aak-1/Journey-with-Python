def anagrams(word, words):
    #your code here
    a = sorted(word)
    b = ''.join(a)
    a = []
    for i in words:
        c = sorted(i)
        j = ''.join(c)
        if j == b:
            a.append(i)
    return a 