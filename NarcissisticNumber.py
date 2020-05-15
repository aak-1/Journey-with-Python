def narcissistic( value ):
    # Code away
    a = 0
    c = len(str(value))
    for i in list(str(value)):
        a += (int(i)**c)
    if a == value:
        return True
    else:
        return False