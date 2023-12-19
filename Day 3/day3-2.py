file = open("input.txt")
line_length = len(open("input.txt").readline()) + 1
data = ['.' * line_length] + ['.' + line.rstrip('\n') + '.' for line in file.readlines()] + ['.' * line_length]
value = 0
adjacent_to_star = {}


def check_number(number, number_row, number_col):
    for y in range(number_col - len(number), number_col):
        adjacent_chars = [data[number_row - 1][y - 1], data[number_row - 1][y],
                          data[number_row - 1][y + 1], data[number_row][y - 1],
                          data[number_row][y + 1], data[number_row + 1][y - 1],
                          data[number_row + 1][y], data[number_row + 1][y + 1]]
        char_indexes = [(number_row - 1, y - 1), (number_row - 1, y),
                        (number_row - 1, y + 1), (number_row, y - 1),
                        (number_row, y + 1), (number_row + 1, y - 1),
                        (number_row + 1, y), (number_row + 1, y + 1)]
        for index, char in enumerate(adjacent_chars):
            if char == "*":
                if adjacent_to_star.keys().__contains__(char_indexes[index]):
                    adjacent_to_star[char_indexes[index]][0] *= int(number)
                    adjacent_to_star[char_indexes[index]][1] += 1
                    return
                else:
                    adjacent_to_star[char_indexes[index]] = [int(number), 1]
                    return


for row in range(1, len(data) - 1):
    current_number = ''
    for col in range(1, line_length):
        if data[row][col].isdigit():
            current_number += data[row][col]
        else:
            check_number(current_number, row, col)
            current_number = ''
for adjacent in adjacent_to_star.values():
    if adjacent[1] == 2:
        value += adjacent[0]
print(value)
