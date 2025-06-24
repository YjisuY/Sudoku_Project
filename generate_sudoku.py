import random
from solve_sudoku import solve_sudoku
from initialize_board import initialize_board

def generate_sudoku():
    board = initialize_board()
    # 임의로 숫자 몇 개 넣기
    for _ in range(10):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0:
            board[row][col] = num
            if not solve_sudoku([row[:] for row in board]):
                board[row][col] = 0
    return board
