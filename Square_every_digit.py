def square_digits(num):
    a = str(num) 
    b = ''
    for i in range(len(a)):
        b+=(str(int(a[i])**2))
    return int(b)