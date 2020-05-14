def accum(s):
    # your code
    stringg = list(s)
    res = ''
    count = 1
    for i in stringg:
        res += (str(i)*count).capitalize()
        res += '-'
        count += 1
        
    st = list(res)
    del st[-1]
    res = (''.join(str(x) for x in st))
    return res