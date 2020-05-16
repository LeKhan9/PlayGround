from math import sqrt


START_ROW = START_COL = 0
EMPTY_VAL_MARKER = '.'


def solve_sudoku(board):
    solve(START_ROW, START_COL, board)


def solve(row, col, board):
    if col == len(board[row]):
        col = START_COL
        row += 1

        if row == len(board):
            return True

    if board[row][col] != EMPTY_VAL_MARKER:
        return solve(row, col + 1, board)

    for i in range(1, len(board) + 1):
        char_option = str(i)

        if is_valid_placement(board, row, col, char_option):
            board[row][col] = char_option


            if solve(row, col + 1, board):
                return True

            # backtrack
            board[row][col] = EMPTY_VAL_MARKER

    return False


def is_valid_placement(board, row, col, char_option):
    for val in board[row]:
        if val == char_option:
            return False

    for row_arr in board:
        if row_arr[col] == char_option:
            return False

    num_blocks = int(sqrt(len(board)))

    start_row_block = (row // num_blocks) * num_blocks
    start_col_block = (col // num_blocks) * num_blocks

    for i in range(num_blocks):
        for j in range(num_blocks):
            if char_option == board[start_row_block + i][start_col_block + j]:
                return False

    return True


def print_board(board):
    for row in board:
        print(row)


def run_example():
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

    solve_sudoku(board)
    print_board(board)


if __name__ == '__main__':
    run_example()
