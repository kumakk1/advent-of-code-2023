file = open("input.txt")
data = [line.rstrip("\n") for line in file.readlines()]
value = 0
for line in data:
    index_first = len(line)
    index_last = 0
    for index, char in enumerate(line):
        if char.isdigit():
            if index >= index_last:
                index_last = index
            if index <= index_first:
                index_first = index
    value += int(line[index_first] + line[index_last])
print(value)
