from random import randint
import prompt
from BRAIN_GAMES.cli import name


def iseven():
    right_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while right_answers < 3:
        number = randint(1, 100)
        iseven_check = number % 2
        print(number)
        answer = prompt.string('')
        if iseven_check == 0 and answer == 'yes':
            right_answers += 1
            print('Correct!')
        elif iseven_check != 0 and answer == 'no':
            right_answers += 1
            print('Correct!')
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was 'no'.\n
            Let's try again, {name}""")
            return
    if right_answers == 3:
        print(f'Congratulations, {name}')


iseven()
