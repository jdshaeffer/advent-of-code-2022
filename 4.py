'''
- split by comma
- split by dash
- make two sets of the ranges
- get the set intersection of each one and see if one is the same length as
  another
'''

with open("input/4") as file:
    input = [line.rstrip() for line in file]

count_complete_overlap = 0
count_any_overlap = 0
for line in input:
    pair = line.split(',')
    first = pair[0].split('-')
    second = pair[1].split('-')
    set1 = {i for i in range(int(first[0]), int(first[1])+1)}
    set2 = {i for i in range(int(second[0]), int(second[1])+1)}
    num_intersect = len(list(set1 & set2))
    if num_intersect == len(list(set1)) or num_intersect == len(list(set2)):
        count_complete_overlap += 1
    if len(list(set1 & set2)):
        count_any_overlap += 1

print(count_complete_overlap)
print(count_any_overlap)

