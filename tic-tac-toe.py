import os

'''
This dictionary will keep track of all the positions in the game.
The board layout looks like this:
   |   |         1 | 2 | 3
---+---+---     ---+---+---
   |   |         4 | 5 | 6
---+---+---     ---+---+---
   |   |         7 | 8 | 9

In the beginning each position will be empty.
As the game progresses, the positions will be filled with Xs and Ys.
'''
positions = {
    1:' ',
    2:' ',
    3:' ',
    4:' ',
    5:' ',
    6:' ',
    7:' ',
    8:' ',
    9:' '
}

#This is a tuple of all possible wins.
possible_wins = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
)

#Used to keep track of number of turns. The main loop will exit when this reaches 9 and the game will end in a draw.
turn_counter = 0
#Used to keep track of whose turn it is and what mark s/he uses.
current_turn = [1, 'O']


def print_divider():
    print("---+---+---\t---+---+---", end='\n')
    
def print_row(n):
    n = n*3
    print(f' {positions[1+n]} | {positions[2+n]} | {positions[3+n]} \t {1+n} | {2+n} | {3+n} ', end = '\n')

#Prints the tic-tac-toe board    
def print_grid():
    print_row(0)
    print_divider()
    print_row(1)
    print_divider()
    print_row(2)

#Tells user the input is invalid
def bad_input():
    print('You have failed in selecting a proper choice. Try again.')

#Sets the position to X or Y. Returns true if successful. If the position is already occupied, it will return false.
def set_position(choice, ox):
    if positions[choice] == 'O' or positions[choice] == 'X':
        return False
    else:
        positions[choice] = ox
        return True

#Check for a winner.    
def check_win_condition():
    for i in range(0, len(possible_wins)):
        a = positions[possible_wins[i][0]]
        b = positions[possible_wins[i][1]]
        c = positions[possible_wins[i][2]]
        if a == b and b == c and a != ' ':
            print(f"Player {current_turn[0]} wins!")
            return True
    return False


print("It's time to T-T-Tic-Tac-Toe!")
print_grid()
while turn_counter < 9:
    print(f"Player {current_turn[0]}'s turn. Choose where to place your {current_turn[1]}: ")
    
    #User input validation loop
    while True:
        #Is the input an integer?
        s = input()
        if s.isdigit():
            choice = int(s)
            #Is the input in the range of 1-9?
            if choice >= 1 and choice <= 9:
                if set_position(choice, current_turn[1]):
                    break
                else:
                    bad_input()
            else:
                bad_input()
        else:
            bad_input()
    

      
    #Clear the console
    os.system('cls')
    #Update the board
    print_grid()
    #Check for a winner
    if check_win_condition():
        break
    #Update turn variables
    if current_turn[0] == 1:
        current_turn = [2, 'X']
    else:
        current_turn = [1, 'O']
    turn_counter += 1

#Check for a draw
if turn_counter == 9:
    print('Draw!')