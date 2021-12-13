LINE_START = "+-------+-------+-------+"
LINE_CELL_PADDING = "|       |       |       |"
CELL_START = "|   "
CELL_END = "   "
COMPUTER_MOVE = 'X'
USER_MOVE = 'O'
board = []


def init_board():
    
    for x in range(0,3):
        board.append([])
        for y in range(0,3):           
            board[x].append((3*x) + y + 1)
        print(board[x])

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    for x in range(len(board)):
        print(LINE_START)
        print(LINE_CELL_PADDING)
        new_line=''
        for y in range(len(board[0])):
            new_line = new_line + CELL_START + str(board[x][y]) + CELL_END
        new_line = new_line + CELL_START
        print(new_line)
        print(LINE_CELL_PADDING)
    print(LINE_START)
    


def enter_move(board):
    free_fields = make_list_of_free_fields(board)   
    move = int(input("Input your next move in the range 1 to 9: "))
    if move not in range(1,10):
        print("Not a valid move!")
        return
    for tup in free_fields:
        
        if move == board[tup[0]][tup[1]]:
            board[tup[0]][tup[1]] = USER_MOVE
            return
            

def make_list_of_free_fields(board):    
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] != USER_MOVE and board[x][y] != COMPUTER_MOVE:
                free_fields.append((x,y))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    # Check rows
    x=0
    y=0
    for x in range(len(board)):
        victory_row = True
        for y in range(len(board[0])):
            victory_row = victory_row and board[x][y] == sign
        if victory_row:
            return True
    print("have checked rows ok")
    x=0
    y=0
    #Check columns
    for y in range(len(board[0])):
        victory_column = True
        for x in range(len(board)):
           victory_column = victory_column and board[x][y] == sign
        if victory_column:
            return True
    
    x=0
    y=0
    #Check diagonals
    victory_first_diag = True
    for x in range(len(board)):
        victory_first_diag = victory_first_diag and board[x][x] == sign
    if victory_first_diag:
        return True

    
    y=0
    #Check second diagonal
    victory_second_diag = True
    for y in range(len(board[0])):
        x=2-y
        victory_second_diag = victory_second_diag and board[x][y] == sign
    if victory_second_diag:
        return True

    return False
                   
""""
def draw_move(board):
    print()
    
    # The function draws the computer's move and updates the board.

"""
init_board()
free_fields = make_list_of_free_fields(board)
victory = False
while free_fields != [] and victory==False:
    display_board(board)
    print(free_fields)
    enter_move(board)
    victory = victory_for(board, USER_MOVE)
    if (victory):
        print("Victory for: ", USER_MOVE ("!")
    free_fields = make_list_of_free_fields(board)

