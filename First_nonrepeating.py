import string
def first_non_repeating_letter(string):
    #your code here
    count = 0
    lowstr = string.lower()
    for i in range(len(string)):
        count = lowstr.count(lowstr[i])
        if count == 1:
            return string[i]
    return ''