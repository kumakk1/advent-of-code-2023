file = open("input.txt")
data = [line.rstrip("\n").split(" ") for line in file.readlines()]
value = 0
for index in range(len(data)):
    data[index] = [data[index][i:i + 2] for i in range(0, len(data[index]), 2)]
    valid = True
    for cubes in data[index]:
        if not cubes[1].find("red"):
            valid = int(cubes[0]) <= 12 and valid
        if not cubes[1].find("green"):
            valid = int(cubes[0]) <= 13 and valid
        if not cubes[1].find("blue"):
            valid = int(cubes[0]) <= 14 and valid
    if valid:
        value += index + 1
print(value)
