second_list = []
third_list = []
cells = []


def isWinner(board, sign):
    return ((board[6] == sign and board[7] == sign and board[8] == sign) or  # across the top
            (board[3] == sign and board[4] == sign and board[5] == sign) or  # across the middle
            (board[0] == sign and board[1] == sign and board[2] == sign) or  # across the bottom
            (board[6] == sign and board[3] == sign and board[0] == sign) or  # down the left side
            (board[7] == sign and board[4] == sign and board[1] == sign) or  # down the middle
            (board[8] == sign and board[5] == sign and board[2] == sign) or  # down the right side
            (board[6] == sign and board[4] == sign and board[2] == sign) or  # diagonal
            (board[8] == sign and board[4] == sign and board[0] == sign))  # diagonal


def init():
    global second_list, third_list, cells
    second_list = [1, 3, 7, 9]
    third_list = [2, 4, 6, 8]
    cells = ['-' for i in range(9)]


def recv_input():
    input_pos = input("Enter position: ")
    if not input_pos.isdigit() or int(input_pos) > 9:
        print("Invalid input! please enter a number between 1-9.")
        return False
    global cells
    idx = int(input_pos) - 1
    if cells[idx] == '-':
        cells[idx] = 'X'
        return True
    else:
        print("Cell already taken!")
        return False


def find_first(lst):
    for i in lst:
        if cells[i - 1] == '-':
            return i
    return False


def machine_choice():
    global cells
    if cells[4] == '-':
        cells[4] = 'O'
    elif type(find_first(second_list)) == int:
        cells[find_first(second_list) - 1] = "O"
    elif type(find_first(third_list)) == int:
        cells[find_first(third_list) - 1] = "O"


def print_board():
    for j in range(3):
        for i in range(3):
            print(cells[3*j + i] + ' ', end=' ')
        print('\n')


init()

while not isWinner(cells, 'X') and not isWinner(cells, 'O') and '-' in cells:
    ok = recv_input()
    while not ok:
        ok = recv_input()
    print_board()
    print('---------')
    machine_choice()
    print_board()

if isWinner(cells, 'X'):
    print("You won!")
elif isWinner(cells, 'O'):
    print("The machine won!")
else:
    print("Draw")


