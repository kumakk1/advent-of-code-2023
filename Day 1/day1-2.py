file = open("input.txt")
data = [line.rstrip("\n") for line in file.readlines()]
value = 0
for line in data:
    index_first = len(line)
    index_last = 0
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    for index, char in enumerate(line):
        if char.isdigit():
            if index >= index_last:
                index_last = index
            if index <= index_first:
                index_first = index
    value += int(line[index_first] + line[index_last])
print(value)
