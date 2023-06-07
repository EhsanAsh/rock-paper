import random
from emoji import emojize
player_wins = 0
computer_wins = 0
while True :
    print(f'player: {player_wins}, computer: {computer_wins}')
    print(emojize(':gem_stone:'))
    print(emojize(':newspaper:'))
    print(emojize(':scissors:'))
    if player_wins == 2:
        print(
            f'Player {player_wins}, computer {computer_wins}. Player wins the game!' +
            emojize('🤩') + emojize('💪')
        )
        break
    elif computer_wins == 2:
        print(f'Player {player_wins}, computer {computer_wins}. Computer wins the game!' + emojize('🤦‍♀️') + emojize('🤷‍♀️')
        )
        break
    else:
        player = input('Player, Please enter your choice:\n')
        computer = random.randint(0, 2)
        if player:
                if player == 'rock':
                    if computer == 0:
                        print('AI chose rock')
                        print('It is a tie!')
                    elif computer == 1:
                        print('AI chose paper')
                        print('computer wins!')
                        computer_wins += 1
                    else:
                        print('AI chose scissors')
                        print('player wins!')
                        player_wins += 1
                if player == 'paper':
                    if computer == 0:
                        print('AI chose rock')
                        print('player wins!')
                        player_wins += 1
                    elif computer == 1:
                        print('AI chose paper')
                        print('It is a tie!')
                    else:
                        print('AI chose scissors')
                        print('computer wins!')
                        computer_wins += 1
                if player == 'scissors':
                    if computer == 0:
                        print('AI chose rock')
                        print('computer wins!')
                        computer_wins += 1
                    elif computer == 1:
                        print('AI chose paper')
                        print('player wins!')
                        player_wins += 1
                    else:
                        print('AI chose scissors')
                        print('It is a tie!')
        else:
            print('Player did not enter his \ her choice correctly. Please enter your choice again!')
