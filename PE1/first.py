

def display_board(board):
    print(board)
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):  
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    print()

def make_list_of_free_fields(board):
    
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    print()

def victory_for(board, sign):
    
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    print()

def draw_move(board):
    print()
    
    # The function draws the computer's move and updates the board.

board = list(range(1,10))
display_board(board)
