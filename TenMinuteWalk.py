def is_valid_walk(walk):
    #determine if walk is valid
    if len(walk) != 10:
        return False
    else:
        ns = 0
        ew = 0
        for i in walk:
            if i == 'n':
                ns += 1
            if i == 'e':
                ew += 1
            if i == 's':
                ns -= 1
            if i == 'w':
                ew -= 1
        if ns == 0 and ew == 0:
            return True
        else: 
            return False