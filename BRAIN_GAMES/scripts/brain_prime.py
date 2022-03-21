from random import randint
import prompt
from BRAIN_GAMES.cli import welcome_user
from BRAIN_GAMES.scripts.brain_games import ender


def isprime(number):
    if number % 2 != 0 and number != 2:
        return (True, 'yes')
    else:
        return (False, 'no')


def prime(user_name):
    right_answers_count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while right_answers_count < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('')
        if isprime(number)[0] is True and answer == 'yes':
            right_answers_count += 1
            print(f'Your answer: {answer}\nCorrect!')
        elif isprime(number)[0] is False and answer == 'no':
            right_answers_count += 1
            print(f'Your answer: {answer}\nCorrect!')
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was {isprime(number)[1]}.\n
            Let's try again, {user_name}""")
            return
    ender(right_answers_count, user_name)


prime(welcome_user())
