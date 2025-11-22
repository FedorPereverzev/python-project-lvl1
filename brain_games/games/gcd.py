from brain_games.utils import is_gcd, random_number


def gcd():

    number_1, number_2 = random_number(), random_number()

    question = f'Question: {number_1} {number_2}'

    right_answer = str(is_gcd(number_1, number_2))

    return right_answer, question