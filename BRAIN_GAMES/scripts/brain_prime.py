from random import randint
import prompt
from BRAIN_GAMES.cli import welcome_user
from BRAIN_GAMES.scripts.brain_games import ender


def main():
    pass


def isprime(number):
    i = 0
    prime_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                   47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    while i < len(prime_tuple):
        if prime_tuple[i] == number:
            return (True, 'yes')
        else:
            i += 1
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
            Let's try again, {user_name}!""")
            return
    ender(right_answers_count, user_name)


prime(welcome_user())
