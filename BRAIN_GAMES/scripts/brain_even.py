from random import randint
import prompt
from BRAIN_GAMES.cli import welcome_user
from BRAIN_GAMES.scripts.brain_games import ender, _main


def iseven(user_name):
    right_answers_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while right_answers_count < 3:
        number = randint(1, 100)
        iseven_check = number % 2
        print(f'Question: {number}')
        answer = prompt.string('')
        if iseven_check == 0 and answer == 'yes':
            right_answers_count += 1
            print('Correct!')
        elif iseven_check != 0 and answer == 'no':
            right_answers_count += 1
            print('Correct!')
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was 'no'.\n
            Let's try again, {user_name}""")
            return
    ender(right_answers_count, user_name)


iseven(welcome_user())
