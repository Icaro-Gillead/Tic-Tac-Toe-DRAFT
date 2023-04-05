# TIC TAC TOE GAME: DRAFT TO USE AS BASIS FOR A MORE ADVANCED GAME

tictac = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
refer = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print('Type the letter corresponding to the desired position ↓')
print('a|b|c\nd|e|f\ng|h|i')

# Player's names input by the users
player_1 = str(input('Type the 1st player name: ')).strip().title()
player_2 = str(input('Type the 2nd player name: ')).strip().title()

# 'fim' is to control when to end the program: when someone win or someone choose to,+
# + by lefting the game's input empty (enter to stop!)
fim = 0
players = {1: player_1, 2: player_2}

# function designed to input the user's position in the game's. 'rodar' is to avoid printing the tic tac +
# + toe one above another print with the same result (it will happen if you remove the 'rodar' variable).
def game1(current_player):
    global fim
    other_player = 3 - marca
    rodar = 0
    x = str(input(f'{current_player}, type the position you want to fill (Enter to stop!): ')).strip().lower()
    if x == '':
        fim = 1
    for i, var in enumerate(refer):
        if var == x:
            if tictac[i // 3][i % 3] == 0:
                tictac[i // 3][i % 3] = marca
            elif tictac[i // 3][i % 3] == marca:
                print('You already filled this slot, choose another!')
                rodar = 1
                game1(current_player)
            elif current_player == players[marca]:
                print(f'Player {other_player}, {players[other_player]} already choose this slot. Choose another!')
                rodar = 1
                game1(current_player)
    if rodar == 0:
        for c in range(3):
            print(tictac[c])


# function to verify the winner
def verify_winner():
    c = 0
    global fim
    for d in range(3):
        if tictac[d][0] == marca and tictac[d][1] == marca and tictac[d][2] == marca:
            print(f'Player {marca}: {players[marca]} WIN!')
            fim = 1
        elif tictac[0][d] == marca and tictac[1][d] == marca and tictac[2][d] == marca:
            print(f'Player {marca}: {players[marca]} WIN!')
            fim = 1
    if tictac[0][0] == marca and tictac[1][1] == marca and tictac[2][2] == marca:
        print(f'Player {marca}: {players[marca]} WIN!')
        fim = 1
    elif tictac[2][0] == marca and tictac[1][1] == marca and tictac[0][2] == marca:
        print(f'Player {marca}: {players[marca]} WIN!')
        fim = 1

    # DRAW code below needs to be updated yet (it doesn't work when the winner will win in the last slot of+
    # + the grid)
    for k in range(3):
        if tictac[k][0] != 0 and tictac[k][1] != 0 and tictac[k][2] != 0:
            c += 1
            if fim != 1 and c == 3:
                fim = 1
                print('DRAW!!')


while True:
    marca = 1
    game1(player_1)
    verify_winner()
    if fim == 1:
        break
    marca = 2
    game1(player_2)
    verify_winner()
    if fim == 1:
        break
