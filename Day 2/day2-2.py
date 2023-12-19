file = open("input.txt")
data = [line.rstrip("\n").split(" ") for line in file.readlines()]
value = 0
for index in range(len(data)):
    data[index] = [data[index][i:i + 2] for i in range(0, len(data[index]), 2)]
    rgb_max = [0, 0, 0]
    for cubes in data[index]:
        if not cubes[1].find("red"):
            rgb_max[0] = max(rgb_max[0], int(cubes[0]))
        if not cubes[1].find("green"):
            rgb_max[1] = max(rgb_max[1], int(cubes[0]))
        if not cubes[1].find("blue"):
            rgb_max[2] = max(rgb_max[2], int(cubes[0]))
    value += rgb_max[0] * rgb_max[1] * rgb_max[2]
print(value)
