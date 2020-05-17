def solve_n_queens(n):
    '''
        Given input N, generates an NxN Chess Board where there are N queens placed in
        such a way that no queen is attacking another queen.
    '''

    boards = []
    solve(0, n, [], boards)
    return boards


def solve(row, n, placements, boards):
    if row == n:
        board = generate_board_matrix(placements)
        boards.append(board)
        return

    for col in range(0, n):
        placements.append(col)

        if is_valid(placements):
            solve(row + 1, n, placements, boards)

        placements.pop() # backtrack col placements


def is_valid(placements):
    curr_row = len(placements) - 1

    for prev_row in range(0, curr_row):
        column_diff = abs(placements[prev_row] - placements[curr_row])
        row_diff = curr_row - prev_row
        diag_diff = column_diff - row_diff

        if column_diff == 0 or diag_diff == 0:
            return False

    return True


def generate_board_matrix(placements):
    board = []

    for row in range(len(placements)):
        output = ""

        for col in range(len(placements)):
            if col == placements[row]:
                output += 'Q'
            else:
                output += '-'

        board.append(output)

    return board


def print_boards(boards):
    for i, board in enumerate(boards):
        print(f'\nOutput Board # {i + 1}')

        for row in board:
            beautified_row = row.replace('Q', ' Q ').replace('-', ' _ ')
            print(f'[{beautified_row}]')


def run_example():
    NUM_QUEENS = 4
    boards = solve_n_queens(NUM_QUEENS)
    print_boards(boards)

    ''''
    Output Board # 1
    [ _  Q  _  _ ]
    [ _  _  _  Q ]
    [ Q  _  _  _ ]
    [ _  _  Q  _ ]
    
    Output Board # 2
    [ _  _  Q  _ ]
    [ Q  _  _  _ ]
    [ _  _  _  Q ]
    [ _  Q  _  _ ]
    '''


if __name__ == '__main__':
    run_example()
