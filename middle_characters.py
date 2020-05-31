def get_middle(s):
    if len(s)%2 == 0:
        a = list(s)
        n = int(len(s)/2)
        b = ''.join(a[n-1:n+1])
        return b
    else:
        n = int(len(s)/2)
        #print(n)
        a = list(s)
        return a[n]
    #your code here