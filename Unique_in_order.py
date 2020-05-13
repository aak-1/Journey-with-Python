def unique_in_order(iterable):
    lame = list(iterable)
    a = len(iterable)
    arr = []
    if a > 0:
        arr = [lame[0]]
        for i in range (0, a - 1):
            if lame[i] != lame[i + 1]:
                arr.append(lame[i + 1])
<<<<<<< HEAD
    return arr
#codewars
    
=======
    return arr
>>>>>>> 93a42e3e65be2055d449e33203052debd1af8582
