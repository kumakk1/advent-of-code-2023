file = open("input.txt")
data = [line.rstrip('\n').split(" | ") for line in file]
value = 0
for line in data:
    points = 0.5
    winning_numbers = line[0].split(" ")
    current_numbers = line[1].split(" ")
    for number in current_numbers:
        if number in winning_numbers and number.isdigit():
            points *= 2
    value += int(points)
print(value)
