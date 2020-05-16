def move_zeros(array):
    #your code here
    res = []
    count = 0
    for i in array:
        if i == '0':
            res.append(i)
        elif '0' == str(i) or '0.0' == str(i):
            count += 1
        else:
            res.append(i)
    for i in range (count):
        res.append(0)
    return res