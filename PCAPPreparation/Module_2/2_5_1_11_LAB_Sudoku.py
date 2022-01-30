'''Sudoku Validation Lab 2.5.1.11'''

sudoku = []
row = ""
valid_sudoku = True
invalid_data = True
while invalid_data:
    """data = input("Enter your 9 digit rows separated by space: ")"""
    data = "195743862 431865927 876192543 387459216 612387495 549216738 763524189 928671354 254938671"
    sudoku = data.split(" ")

    if len(sudoku) < 9:
        invalid_data = True
        continue
    for row in sudoku:
        if len(row) < 9:
            invalid_data = True
            continue
    invalid_data = False


# Validate rows
for row in sudoku:
    for i in range(1, 10):
        if chr(i) not in row:
            valid_sodoku = False
            break
if not valid_sudoku:
    print(f"No, Sudoku not valid - row validation: row {row} char {chr(i)}")
    exit()

# Validate columns
for j in range(9):
    column_str = ""
    for row in sudoku:
        column_str = column_str + row[j]
    # print("Next column str:", column_str)
    # Validate column string
    for k in range(1, 10):
        if chr(k) not in column_str:
            valid_sodoku = False
            break
    if not valid_sudoku:
        print(f"No Sudoku not valid column validation. Column: {j} Column string {column_str} char {chr(k)}")
        exit()

# Validate subsquares

sudoko_array = [[sudoku[i][j] for i in range(0, 9)] for j in range(0, 9)]
board = ""
for column in range(0, 9, 3):
    for row in range(0, 9, 3):
        for offset in range(0, 3):
            board += sudoku[row + offset][column:column + 3]
            board_sorted = "".join(sorted(board))
            if board_sorted != "123456789":
                valid_sodoku = False
                break
    if not valid_sudoku:
        print(f"No Sudoku not valid subsquare validation. Board: {board}")
        exit()


print("Yes Sudoku valid")
