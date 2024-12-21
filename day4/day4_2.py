with open("./input.txt") as file_input:
    grid_lines = file_input.read().strip().split("\n")

num_rows = len(grid_lines)
num_cols = len(grid_lines[0])

directions = []
for delta_x in range(-1, 2):
    for delta_y in range(-1, 2):
        if delta_x != 0 or delta_y != 0:
            directions.append((delta_x, delta_y))

def has_xmas(row, col):
    if not (1 <= row < num_rows - 1 and 1 <= col < num_cols - 1):
        return False
    if grid_lines[row][col] != "A":
        return False

    # Check both diagonals
    diagonal_1 = f"{grid_lines[row-1][col-1]}{grid_lines[row+1][col+1]}"
    diagonal_2 = f"{grid_lines[row-1][col+1]}{grid_lines[row+1][col-1]}"

    return diagonal_1 in ["MS", "SM"] and diagonal_2 in ["MS", "SM"]

count_xmas = 0
for row in range(num_rows):
    for col in range(num_cols):
        count_xmas += has_xmas(row, col)

print(count_xmas)