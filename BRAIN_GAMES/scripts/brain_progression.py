from random import randint
import prompt
from BRAIN_GAMES.cli import welcome_user
from BRAIN_GAMES.scripts.brain_games import ender


def main():
    pass


def prog_maker(length, position, step_value):
    result = ''
    hidden_number = ''
    step = step_value
    i = 1
    while i <= length:
        if i == position:
            result += '.. '
            step += step_value
            hidden_number = step
            i += 1
        else:
            i += 1
            step += step_value
            result += f'{str(step)} '
    return (result, str(hidden_number))


def progression(user_name):
    right_answers_count = 0
    prgrs = ''
    print('Find the greatest common divisor of given numbers.')
    while right_answers_count < 3:
        progression_length = randint(5, 10)
        hidden_position = randint(1, progression_length)
        step_value = randint(0, 10)
        prgrs = prog_maker(progression_length, hidden_position, step_value)
        right_answer = prgrs[1]
        print(f'Question: {prgrs[0]})
        answer = prompt.string('')
        if answer == prgrs[1]:
            right_answers_count += 1
            print(f'Your answer: {answer}\nCorrect!')
        else:
            print(f"""{answer} is wrong answer ;(. Correct answer was {right_answer}.\n
            Let's try again, {user_name}!""")
            return
    ender(right_answers_count, user_name)


progression(welcome_user())
