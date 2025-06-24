from generate_sudoku import generate_sudoku
from print_board import print_board
from solve_sudoku import solve_sudoku

def play_sudoku():
    board = generate_sudoku()
    print("Welcome to Sudoku!")
    print_board(board)
    # 실제 플레이 기능은 간단화
    print("\nAuto-solving...")
    solve_sudoku(board)
    print("\nSolved Sudoku:")
    print_board(board)
