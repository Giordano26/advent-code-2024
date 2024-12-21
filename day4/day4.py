def find_xmas_in_grid(lines):
    row_len = len(lines)
    column_len = len(lines[0])
    count = 0
    xmas = "XMAS"

    for row_index in range(row_len):
        for column_index in range(column_len):
            # Check horizontally to the right
            if column_index + 3 < column_len:
                if lines[row_index][column_index:column_index+4] == xmas:
                    count += 1

            # Check horizontally to the left
            if column_index - 3 >= 0:
                if lines[row_index][column_index:column_index-4:-1] == xmas:
                    count += 1

            # Check vertically downwards
            if row_index + 3 < row_len:
                if ''.join([lines[row_index+i][column_index] for i in range(4)]) == xmas:
                    count += 1

            # Check vertically upwards
            if row_index - 3 >= 0:
                if ''.join([lines[row_index-i][column_index] for i in range(4)]) == xmas:
                    count += 1

            # Check diagonally down-right
            if row_index + 3 < row_len and column_index + 3 < column_len:
                if ''.join([lines[row_index+i][column_index+i] for i in range(4)]) == xmas:
                    count += 1

            # Check diagonally down-left
            if row_index + 3 < row_len and column_index - 3 >= 0:
                if ''.join([lines[row_index+i][column_index-i] for i in range(4)]) == xmas:
                    count += 1

            # Check diagonally up-right
            if row_index - 3 >= 0 and column_index + 3 < column_len:
                if ''.join([lines[row_index-i][column_index+i] for i in range(4)]) == xmas:
                    count += 1

            # Check diagonally up-left
            if row_index - 3 >= 0 and column_index - 3 >= 0:
                if ''.join([lines[row_index-i][column_index-i] for i in range(4)]) == xmas:
                    count += 1

    return count

with open('./input.txt', 'r') as file:
    lines = file.read().strip().split("\n")

xmas_count = find_xmas_in_grid(lines)
print(xmas_count)