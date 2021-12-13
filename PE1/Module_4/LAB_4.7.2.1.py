LINE_START = "+-------+-------+-------+"
LINE_CELL_PADDING = "|       |       |       |"
CELL_START = "|   "
CELL_END = "   "
X = 'X'
O = 'O'
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
        row = int(tup[0])
        col = int(tup[1])
        if move == board[tup[0]][tup[1]]:
            board[tup[0]][tup[1]] = O
            return
            

def make_list_of_free_fields(board):
    
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] != X and board[x][y] != O:
                free_fields.append((x,y))
    return free_fields
"""
def victory_for(board, sign):
    
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    print()

def draw_move(board):
    print()
    
    # The function draws the computer's move and updates the board.

"""
init_board()
display_board(board)
free_fields = make_list_of_free_fields(board)
while free_fields != []:
    print(free_fields)
    enter_move(board)
    display_board(board)
    free_fields = make_list_of_free_fields(board)

