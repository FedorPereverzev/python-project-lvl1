from random import randint
import prompt
from BRAIN_GAMES.cli import name
from BRAIN_GAMES.scripts.brain_games import ender


def calc():
    right_answers_count = 0
    print('What is the result of the expression?')
    while right_answers_count < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        sum = number1 + number2
        minus = number1 - number2
        mult = number1 * number2
        operations = ('+', '-', '*')
        random = randint(0, 2)
        rand_operations = operations[random]
        answers = (sum, minus, mult)
        right_answer = answers[random]
        print(f'Question: {number1} {rand_operations} {number2}')
        answer = prompt.string('')
        if rand_operations == '+' and answer == str(sum):
            right_answers_count += 1
            print(f'Your answer: {answer}\nCorrect!')
        elif rand_operations == '-' and answer == str(minus):
            right_answers_count += 1
            print(f'Your answer: {answer}\nCorrect!')
        elif rand_operations == '*' and answer == str(mult):
            right_answers_count += 1
            print(f'Your answer: {answer}\nCorrect!')
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was {right_answer}.\n
            Let's try again, {name}""")
            return
    ender(right_answers_count)


calc()
