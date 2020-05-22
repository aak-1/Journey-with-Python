def solution(number):
    sum = 0
    for i in range (0, number):
        if ((i % 15) == 0):            
            sum += i
        elif ((i % 5) == 0):
            sum += i          
        elif i % 3 == 0:
            sum += i            
        else:
            pass
    return sum