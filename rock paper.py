import random


print("Let's play rock paper scissors shoot!\n")


options = ['Rock', 'Paper', 'Scissors']
def play():
    you = input('Go ahead and I will generate a random choice right after: ').upper()
    opp = random.choice(options)
    print('Opponents Choice:', opp)
    return you, opp


def winner(you,opp):
    if (you == 'ROCK' and opp == 'Scissors') or \
       (you == 'PAPER' and opp == 'Rock') or \
       (you == 'SCISSORS' and opp == 'Paper'):
        return 'You Win!'

    








play()
