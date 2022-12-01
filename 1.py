with open('input/1') as file:
    input = [int(line.rstrip()) if line != '\n' else -1 for line in file]

max = 0
second_max = 0
third_max = 0
curr_sum = 0
for num in input:
    if num != -1:
        curr_sum += num
    if num == -1:
        if curr_sum > max:
            third_max = second_max
            second_max = max
            max = curr_sum
        elif curr_sum > second_max:
            third_max = second_max
            second_max = curr_sum
        elif curr_sum > third_max:
            third_max = curr_sum
        curr_sum = 0

print(sum([max, second_max, third_max]))

