import random
from emoji import emojize
print(emojize(':gem_stone:'))
print(emojize(':newspaper:'))
print(emojize(':scissors:'))
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
        else:
            print('AI chose scissors')
            print('player wins!')
    if player == 'paper':
        if computer == 0:
            print('AI chose rock')
            print('player wins!')
        elif computer == 1:
            print('AI chose paper')
            print('It is a tie!')
        else:
            print('AI chose scissors')
            print('computer wins!')
    if player == 'scissors':
        if computer == 0:
            print('AI chose rock')
            print('computer wins!')
        elif computer == 1:
            print('AI chose paper')
            print('player wins!')
        else:
            print('AI chose scissors')
            print('It is a tie!')
else:
    print('Player did not enter his \ her choice correctly. Please enter your choice again!')
