from pprint import pprint

with open('input/5') as file:
    input = [line.rstrip() for line in file]

proc = [line.split() for line in input if line and line[0] == 'm']
rows = []
col_count = 0
for line in input:
    if line[1] == '1':
        col_count = int(line.rstrip()[-1])
        break
    rows.append(line.translate({ord(char): None for char in '[]'}))
rows = [row.split(' ') for row in rows]

# 4 spaces represents one skipped column, clean that up and parse
for j, row in enumerate(rows):
    if '' in row:
        for i in range(len(row)):
            if row[i] == '':
                i += 1
                z = 0
                while z < 3:
                    row[i] = '!'
                    i += 1
                    z += 1
        rows[j] = [char for char in row if char != '!']

for row in rows:
    while len(row) < col_count:
        row.append('')

# make stack dict
columns = {i+1: [] for i in range(col_count)}
i = j = 0
while i < len(rows) and j < col_count:
    columns[j+1].append(rows[i][j])
    if i == len(rows) - 1:
        j += 1 
        i = 0
    else:
        i += 1

# rev to make right stack order
for i in range(1, col_count+1):
    columns[i] = [a for a in list(reversed(columns[i])) if a != '']

# move <grouped_quantity> from <col_num> to <col_num>
for p in proc:
    quant = int(p[1])
    s_col = int(p[3])
    e_col = int(p[-1])

    # part 1
    # while quant != 0:
    #     columns[e_col].append(columns[s_col].pop())
    #     quant -= 1

    # part 2
    columns[e_col] += columns[s_col][len(columns[s_col])-quant:len(columns[s_col])]
    columns[s_col] = columns[s_col][:len(columns[s_col])-quant]

print(''.join([val[-1] for _, val in columns.items()]))

