'''
- Every item type is identified by a single lowercase or uppercase letter (that
  is, a and A refer to different types of items).
- chars in first half of string represent items in first compartment of
  rucksack, second half in second compartment
- first find the letter, lowercase or capital, that both halves of the string
  share
    - split the string in half
    - make a hash of the first half
    - iterate the second half, finding the first dup
    - cache the dup in list
    - go to next string
- then assign the letter to their corresponding int val, return sum
- lookup map?
    - a-z = 1-26
    - A-Z = 26-52
- ascii value? NOICE

- part2:
- Every set of three lines in your list corresponds to a single group
- find the only item type that appears in all three strings in a group 
- split the input into groups of three - have a working list to append to, everytime
  length gets to 3, work it, cache result, then delete it and move on to next
  group
- turn each str into a set
- find the intersection of the set of the grouped strings
'''

with open("input/3") as file:
    input = [line.rstrip() for line in file]
dups1 = []
dups2 = []
working_group = []
for str in input:
    # part1
    common_el = set(str[:len(str)//2]) & set(str[len(str)//2:])
    dups1.append(list(common_el)[0])

    # part2
    working_group.append(str)
    if len(working_group) == 3:
        common_el = set(working_group[0]) & set(working_group[1]) & set(working_group[2])
        dups2.append(list(common_el)[0])
        working_group = []

def char_arr_to_val_arr(arr):
    for i, char in enumerate(arr):
        val = ord(char)
        if char in 'abcdefghijklmnopqrstuvwxyz':
            val -= 96
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            val -= 38
        arr[i] = val
    return arr
    
print('part1', sum(char_arr_to_val_arr(dups1)))
print('part2', sum(char_arr_to_val_arr(dups2)))
    
