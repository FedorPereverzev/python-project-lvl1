
from brain_games.cli import welcome_user
from brain_games.utils import random_number, random_operation


def calc(user_name):

    count_of_corrects = 0

    operators = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y}
    
    print('What is the result of the expression?')

    while count_of_corrects < 3:
    
        number_1, number_2 = random_number(), random_number()
        operation = random_operation()
        right_answer = str(operators[operation](number_1, number_2))
        question = [str(number_1), operation, str(number_2)]
        print(f"Question: {' '.join(question)}")

        answer = input()
        print(f'Your answer: {answer}')

        if answer == right_answer:
            print('Correct!')
            count_of_corrects += 1
        else:   
            print(f"'{answer}' is wrong answer ;(. " 
                f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return 

    if count_of_corrects == 3:
        print(f'Congratulations, {user_name}!')
        return 


def main():
    user = welcome_user()
    calc(user)   