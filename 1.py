with open('input/1') as file:
    input = [int(line.rstrip()) if line != '\n' else -1 for line in file]

# find the top 3
max = 0
second_max = 0
third_max = 0
curr_sum = 0
for i,num in enumerate(input):
    if num == -1:
        if curr_sum > max:
            third_max = second_max
            second_max = max
            max = curr_sum
        elif curr_sum > second_max:
            third_max = second_max
            second_max = curr_sum
        elif curr_sum > third_max:
            print('cmon!!')
            third_max = curr_sum
        curr_sum = 0
    else:
        curr_sum += num
    if i == len(input) - 1:
        if curr_sum > max:
            third_max = second_max
            second_max = max
            max = curr_sum
        elif curr_sum > second_max:
            third_max = second_max
            second_max = curr_sum
        elif curr_sum > third_max:
            third_max = curr_sum

print('max', max)
print('second_max', second_max)
print('third_max', third_max)
print('')
print(sum([max, second_max, third_max]))

# print(sum([max, second_max, third_max]))

