def digital_root(n):
    # ...
    sum = 0
    for i in str(n):
        sum += int(i)
    if sum//10 ==0:
        return sum
    else:
        return digital_root(sum)
        