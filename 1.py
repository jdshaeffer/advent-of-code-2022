# find the two entries that sum to 2020
# return their product
'''
- there's the quadratic solution, but that's boring
- find the diff of each one
- convert list into a hash map of indices and component
    {complement: index}
- need index too or we could just make sure that we're not comparing the same
  one together
- constant look up to see if the diff is there - same as google interview prep
  question

- find the 3 numbers that sum up to 2020 - there's only 1
- take the complement dir, 
- 2020-979=1041 so now see if there's anything in the list that could add up to
  1041 - remove all elements that are greater than 1041 (and curr element)
- repeat the complement dict algorithm with the diff in question being 1041
[366, 299, 675]
'''

with open('input/1') as file:
    input = [int(line.rstrip()) for line in file]

# part1
d = {2020-num: i for i, num in enumerate(input)}
for i, num in enumerate(input):
    if num in d and i != d[num]:
        ans = num * (2020-num)

# part2
input = [1721, 979, 366, 299, 675, 1456]
complement_input = [2020-num for num in input]
for comp in complement_input:
    remaining = [num for num in input if num < comp]
    if len(remaining):
        d = set()
        d = {num for num in remaining}
        print(input)
        print(complement_input)
        print(d)
        break


