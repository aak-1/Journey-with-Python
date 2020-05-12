def unique_in_order(iterable):
    lame = list(iterable)
    a = len(iterable)
    arr = []
    if a > 0:
        arr = [lame[0]]
        for i in range (0, a - 1):
            if lame[i] != lame[i + 1]:
                arr.append(lame[i + 1])
    return arr