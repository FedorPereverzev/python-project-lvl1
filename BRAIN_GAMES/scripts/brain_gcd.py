from random import randint
import prompt
from BRAIN_GAMES.cli import welcome_user
from BRAIN_GAMES.scripts.brain_games import ender


def main():
    pass


def gcd_count(mini, maxi):
    i = mini
    while maxi % i != 0 or mini % i != 0:
        i -= 1
    return i


def gcd(user_name):
    right_answers_count = 0
    print('Find the greatest common divisor of given numbers.')
    while right_answers_count < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        numbers_tuple = (number1, number2)
        min_number = min(numbers_tuple)
        max_number = max(numbers_tuple)
        right_answer = gcd_count(min_number, max_number)
        print(f'Question: {number1}  {number2}')
        answer = prompt.string('')
        if answer == str(right_answer):
            right_answers_count += 1
            print(f'Your answer: {answer}\nCorrect!')
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was {right_answer}.\n
            Let's try again, {user_name}!""")
            return
    ender(right_answers_count, user_name)


gcd(welcome_user())
