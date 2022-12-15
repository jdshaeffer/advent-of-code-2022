'''
- tree is visible if all trees between it and edge of grid are shorter than it
- has to only be visible in one direction
- row or column only

- make the matrix map
- mark negative if visible or just have a count as you go along
- visible if on an edge or if its number is greater than all others to the left of
  it or to the right of it or above it or below it
'''
with open('input/8_test') as file:
    mat = [[*line.rstrip()] for line in file]
    for i in range(len(mat)):
        mat[i] = [int(digit) for digit in mat[i]]
# perimeter = 2 * (len(mat) + len(mat[0]))
for i in range(len(mat)):
    for j in range(len(mat[i])):
        curr = mat[i][j]
        print(mat[i][j], end='')
    print()

