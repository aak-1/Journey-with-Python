import re
phonenum = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phonenum.search('my number is 415-555-4242')
mo = phonenum.search('my number is 415-555-4242')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
x = input()

batregex = re.compile(r'bat(mobile|man|bat|copter)')
mo1 = batregex.search('batmobile bathellohello')
print(mo1.group())
input()