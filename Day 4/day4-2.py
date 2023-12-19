file = open("input.txt")
data = [line.rstrip('\n').split(" | ") for line in file]
card_quantity = [1 for _ in range(len(data))]
value = 0
for index, line in enumerate(data):
    points = 1
    winning_numbers = line[0].split(" ")
    current_numbers = line[1].split(" ")
    for number in current_numbers:
        if number in winning_numbers and number.isdigit():
            points += 1
    for _ in range(index + 1, index + points):
        card_quantity[_] += card_quantity[index]
    value += card_quantity[index]
print(value)
