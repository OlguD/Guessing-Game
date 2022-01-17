import random

heart_emoji = "\U0001F49A"

words = ['Hangman', 'Spiderman', 'Batman', 'Discord', 'Youtube', 'Apple',
'Absurd', 'Awkward', 'Avenue', 'Blitz', 'Buzzard', 'Flyby']


def Hangman(heart=5):
    random_word = random.choice(words)
    i = 0
    while i < heart:
        print(f'{heart_emoji} => {heart}')
        guess = input('Guess Some Word:')
        if random_word == guess.capitalize():
            print(f'You win ! with {heart_emoji} => {heart}')
            break
        elif guess.capitalize() != random_word:
            heart-=1
        if heart == 0 :
            print(f'You lost **{random_word}**')
            break
Hangman()
