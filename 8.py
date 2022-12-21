from functools import reduce

'''
- tree is visible if all trees between it and edge of grid are shorter than it
- has to only be visible in one direction
- row or column only

- make the matrix map
- mark negative if visible or just have a count as you go along
- visible if on an edge or if its number is greater than all others to the left of
  it or to the right of it or above it or below it
'''
def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            curr = mat[i][j]
            print(mat[i][j], end='')
        print()

with open('input/8') as file:
    mat = [[*line.rstrip()] for line in file]
    for i in range(len(mat)):
        mat[i] = [int(digit) for digit in mat[i]]

def part_1():
    # -4 since it double counts corners
    perimeter = 2 * (len(mat) + len(mat[0]))-4
    visible = 0
    for i in range(1, len(mat)-1):
        for j in range(1, len(mat[i])-1):
            # it only needs to be visible from one side
            # need to check left, check right, check top, check bottom, all separate
            curr = mat[i][j]
            left = top = 0
            right = len(mat[i])-1
            bottom = len(mat)-1
            check = []

            # left
            while left < j:
                check.append(mat[i][left])
                left += 1
            if all(l < curr for l in check):
                visible += 1
                continue
            else:
                check = []

            # top
            while top < i:
                check.append(mat[top][j])
                top += 1
            if all(t < curr for t in check):
                visible += 1
                continue
            else:
                check = []

            # right
            while right > j:
                check.append(mat[i][right])
                right -= 1
            if all(r < curr for r in check):
                visible += 1
                continue
            else:
                check = []

            # bottom
            while bottom > i:
                check.append(mat[bottom][j])
                bottom -= 1
            if all(b < curr for b in check):
                visible += 1
                continue
            else:
                check = []

    print(visible + perimeter)
def part_2():
    scores = []
    for i in range(1, len(mat)-1):
        for j in range(1, len(mat[i])-1):
            curr = mat[i][j]
            left = j-1
            right = j+1
            top = i-1
            bottom = i+1
            curr_score = 0
            score = []
            # left
            while left >= 0:
                curr_score += 1
                if mat[i][left] >= curr or left == 0:
                    score.append(curr_score)
                    break
                left -= 1
            # right
            curr_score = 0
            while right < len(mat[i]):
                curr_score += 1
                if mat[i][right] >= curr or right == len(mat[i]) - 1:
                    score.append(curr_score)
                    break
                right += 1
            # top
            curr_score = 0
            while top >= 0:
                curr_score += 1
                if mat[top][j] >= curr or top == 0:
                    score.append(curr_score)
                    break
                top -= 1
            # bottom
            curr_score = 0
            while bottom < len(mat):
                curr_score += 1
                if mat[bottom][j] >= curr or bottom == len(mat) -1:
                    score.append(curr_score)
                    break
                bottom += 1
            scores.append(reduce(lambda x, y: x*y, score))
    print('ans', max(scores))

# part_1()
part_2()
