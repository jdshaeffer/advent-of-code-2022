'''
- H and T must always be touching (top/down, left/right, diagonal, and
  overlapping)
- if H is 2 steps directly up, down, left or right from tail, T must move 1 step
  in that same direction
- if H and T are not touching, and they're not in same row or column, T must
  move 1 step diagonally, to get closer and in the same row or column as H
- work out where T goes as H follows the input
- they start out in same position
'''

with open('input/9_test') as file:
    input = [line.rstrip() for line in file]

print(input)
