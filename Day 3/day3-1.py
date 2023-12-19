file = open("input.txt")
line_length = len(open("input.txt").readline()) + 1
data = ['.' * line_length] + ['.' + line.rstrip('\n') + '.' for line in file.readlines()] + ['.' * line_length]
value = 0


def check_number(number, number_row, number_col):
    for y in range(number_col - len(number), number_col):
        adjacent_chars = [data[number_row - 1][y - 1], data[number_row - 1][y],
                          data[number_row - 1][y + 1], data[number_row][y - 1],
                          data[number_row][y + 1], data[number_row + 1][y - 1],
                          data[number_row + 1][y], data[number_row + 1][y + 1]]
        for char in adjacent_chars:
            if char not in "0123456789.":
                return True
    return False


for row in range(1, len(data) - 1):
    current_number = ''
    for col in range(1, line_length):
        if data[row][col].isdigit():
            current_number += data[row][col]
        else:
            if check_number(current_number, row, col):
                value += int(current_number)
            current_number = ''

print(value)
