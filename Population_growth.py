def nb_year(p0, percent, aug, p):
    # your code
    if p0 != p:
        ny = next_year(p0, percent, aug)
        count = 1
        while ny < p:
             ny = next_year(ny, percent, aug)      
             count += 1
    return count
def next_year(p0, percent, aug):
    x = p0 + aug + (percent/100)*p0
    return x
    