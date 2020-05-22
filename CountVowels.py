def getCount(inputStr):
    num_vowels = 0
    # your code here
    for item in inputStr:
        if item in "aeiou":
            num_vowels += 1
    
    return num_vowels