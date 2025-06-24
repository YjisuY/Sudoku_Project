def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, value in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(value if value != 0 else ".", end=" ")
        print()
