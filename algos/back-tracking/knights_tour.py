class ChessBoard():
    # list of offsets of (steps in row direction, steps in col direction)
    ROW_COL_MOVE_OPTIONS = [(2, 1), (1, 2),(-1, 2), (-2, 1), (-2, -1), (-1, -2),(1, -2), (2, -1)]
    UNVISITED_FLAG = -1

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[ChessBoard.UNVISITED_FLAG for col in range(board_size)] for row in range(board_size)]


    def update_board_index(self, row, col, move_num):
        ''' decorate each move with a count '''

        self.board[row][col] = move_num


    def clear_board_index(self, row, col):
        ''' backtrack this move '''

        self.board[row][col] = ChessBoard.UNVISITED_FLAG


    def supports_move_to(self, row, col):
        ''' Next move should be within bounds and to an index that is unvisited '''

        return 0 <= row < self.board_size and \
               0 <= col < self.board_size and \
               self.board[row][col] == ChessBoard.UNVISITED_FLAG


    def is_last_move(self, move_num):
        ''' Have we visited all squares of the chess board '''

        return move_num == self.board_size * self.board_size


    def __str__(self):
        output = ''
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                output += f'{self.board[row][col]}\t'
            output += '\n'
        return output


def knights_tour(board_size):
    chess_board = ChessBoard(board_size)

    start_row = start_col = 0
    move_num = 0

    chess_board.update_board_index(start_row, start_col, move_num)

    if not dfs(chess_board, start_row, start_col, move_num + 1):
        print('No solution found!')
    else:
        print('Solution found: ')
        print(chess_board)


def dfs(chess_board, curr_row, curr_col, move_num):
    if chess_board.is_last_move(move_num):
        return True

    # try all directions
    for row_col_move in chess_board.ROW_COL_MOVE_OPTIONS:
        row_offset, col_offset = row_col_move
        next_row = curr_row + row_offset
        next_col = curr_col + col_offset

        # success ... if this direction lead to a solution
        if chess_board.supports_move_to(next_row, next_col):
            chess_board.update_board_index(next_row, next_col, move_num)

            if dfs(chess_board, next_row, next_col, move_num + 1):
                return True

            # backtrack
            chess_board.clear_board_index(next_row, next_col)

    return False


def run_example():
    board_size = 5

    # generates a chess board of 5x5 dimension with each square labeled in sequence of knight moves such that all
    # squares are visited
    knights_tour(board_size)

    '''
        0	5	14	9	20	
        13	8	19	4	15	
        18	1	6	21	10	
        7	12	23	16	3	
        24	17	2	11	22	
    
    '''


if __name__ == "__main__":
    run_example()
