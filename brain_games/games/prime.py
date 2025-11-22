from brain_games.utils import is_prime, random_number


def prime():

    number = random_number()
    right_answer = is_prime(number)
    question = f'Question: {number}'

    return right_answer, question