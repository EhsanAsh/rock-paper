print('Welcome to Rock, Paper, Scissors game!\n')
player_1 = input('Player 1, Please enter your choice:\n')
print('****No Cheating\n\n'*20)
player_2 = input('Player 2, Please enter your choice:\n')
if player_1 and player_2:
    if player_1 == player_2:
        print("It's a tie!")
    elif player_1 == 'rock':
        if player_2 == 'scissors':
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
    elif player_1 == 'paper':
        if player_2 == 'rock':
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
    elif player_1 == 'scissors':
        if player_2 == 'paper':
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
else:
    print("One or both of players didn't enter their choice. Please enter your choice again!")
