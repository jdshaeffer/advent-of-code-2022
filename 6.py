'''
- find the first occurence of 4 unique chars
- return the len of the str up to that point (at the end of the 4-char seq)
- get windows of substrings, maintain a constant set
- how much time complexity to init a set from a list?
'''

with open('input/6') as file:
    input = [line.rstrip() for line in file]

str = input[0]
for i in range(len(str)-14):
    curr = str[i:i+14]
    set_curr = set(curr)
    if len(curr) == len(set_curr):
        print(i+14)
        break

