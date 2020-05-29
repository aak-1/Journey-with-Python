import string
def duplicate_count(text):
    # Your code goes here
    text1 = text.lower()
    text2 = list(text1)
    n = len(text2)
    count = 0
    for num in range(n):
        if text2[num] in text2[num+1:n]:
            if num == 0:
                count += 1
            if num > 0:
                if text2[num] in text2[0:num]:
                    pass
                else:
                    count += 1
    return count