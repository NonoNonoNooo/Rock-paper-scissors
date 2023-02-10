'''Rock-paper-scissors'''

from random import randint

sl = {1 : 'Rock', 2 : 'Scissors' , 3 : 'Paper'}

def step_bot():

    return randint(1, 3)


bal_player = 0
bal_bot = 0

print('''Hi let’s play scissor rock paper 
your enemy will be a computer 

The winner is determined according to the following rules:

Paper defeats stone («paper wraps stone»).
Stone defeats scissors («stone dulls or breaks scissors»).
Scissors beat paper («scissors cut paper»).''')



def who_win(player, bot):
    global bal_player, bal_bot

    if player == 1:
        if bot == 2:
            bal_player += 1
            return '\n' + 'In this round the player won'.center(40)
        elif bot == 3:
            bal_bot += 1
            return '\n' + 'In this round, the computer won'.center(40)
        else:
            return '\n' + 'Draw'.center(40)
    elif player == 2:
        if bot == 1:
            bal_bot += 1
            return '\n' + 'In this round, the computer won'.center(40)
        elif bot == 3:
            bal_player += 1
            return '\n' + 'In this round the player won'.center(40)
        else:
            return '\n' + 'Draw'.center(40)
    else:
        if bot == 1:
            bal_player += 1
            return '\n' + 'In this round the player won'.center(40)
        elif bot == 2:
            bal_bot += 1
            return '\n' + 'In this round, the computer won'.center(40)
        else:
            return '\n' + 'Draw'.center(40)


while True:

    try:
        rounds = int(input('\nHow many rounds you want to play\nEnter this -> '))
    except:
        print('\nEnter Number PLease')



    for i in range(rounds):
        player_step = input('\nYour move that you choose? Enter a number\nRock -> 1\nScissors -> 2\nPaper -> 3\nIf you want to finish the game write exit\nEnter number or exit -> ')

        if player_step[0] in 'Ee':
            break
        else:
            player_step = int(player_step)

        bot_step = step_bot()

        print('\n','*' * 40)

        print(who_win(player_step, bot_step))

        print('\n','*' * 40)

    print(f'\nYour balls are like this \nPlayer -> {bal_player}\nBot -> {bal_bot}')

    print('\n','*' * 40)

    if bal_bot > bal_player:
        print('\n','Computer won'.center(40))
    elif bal_bot < bal_player:
        print('\n','Player Win'.center(40))
    else:
        print('\n','Draw'.center(40))


    print('\n','*' * 40)

    yes_no = input('\nWant to start over or finish the game\nEnter Yes or no -> ')

    if yes_no[0] in 'Nn':
        print('\nGoodbye')
        break
    else:
        bal_bot, bal_player = 0, 0




