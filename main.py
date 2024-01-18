board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def empty_cell(bo):
    # check for an empty cell
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def is_valid(bo, row, col, num):
    # check for num to be valid in row and col
    for i in range(len(bo[0])):
        if bo[row][i] == num or bo[i][col] == num:
            return False

    # check for num to be valid in 3x3 grid
    for i in range(len(bo[0])):
        if bo[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False

    return True


def solver(bo):
    empty = empty_cell(bo)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(bo, row, col, num):
            bo[row][col] = num
            if solver(bo):
                return True
            else:
                bo[row][col] = 0
    return False


print_board(board)
solver(board)
print("____________________")
print_board(board)
