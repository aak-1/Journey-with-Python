from itertools import combinations

def choose_best_sum(t, k, ls):
    # your code
    iterable = (list(combinations(ls, k)))
    listsum = []
    for i in iterable:
        sumlist = sum(i) 
        listsum.append(sumlist)
    listsum.sort(reverse = True)
    for i in listsum:
        if i <= t:
            return (i)
            break