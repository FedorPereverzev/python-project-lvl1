from brain_games.utils import random_number, random_operation


def calc():

    OPERATORS = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y}

    number_1, number_2 = random_number(), random_number()
    operation = random_operation()
    right_answer = str(OPERATORS[operation](number_1, number_2))
    pre_question = [str(number_1), operation, str(number_2)]
    question = f"Question: {' '.join(pre_question)}"
    return right_answer, question  