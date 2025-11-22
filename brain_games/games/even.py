from brain_games.utils import random_number


def even():
    number = random_number()
    question = f'Question: {number}'
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, question  