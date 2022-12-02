with open("input/2") as file:
    input = [line.rstrip().split(" ") for line in file]

rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
loss = 0
d1 = {
    "A": {"X": rock + draw, "Y": paper + win, "Z": scissors + loss},
    "B": {"X": rock + loss, "Y": paper + draw, "Z": scissors + win},
    "C": {"X": rock + win, "Y": paper + loss, "Z": scissors + draw},
}
total = 0
for round in input:
    total += d1[round[0]][round[1]]

# part 2
d2 = {
    "A": {"X": scissors + loss, "Y": rock + draw, "Z": paper + win},
    "B": {"X": rock + loss, "Y": paper + draw, "Z": scissors + win},
    "C": {"X": paper + loss, "Y": scissors + draw, "Z": rock + win},
}

total = 0
for round in input:
    total += d2[round[0]][round[1]]
print(total)
