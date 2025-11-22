from brain_games.cli import welcome_user
from brain_games.utils import random_number


def even(user_name):

    count_of_corrects = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while count_of_corrects < 3:

        number = random_number()
        print(f'Question: {number}')
        answer = input()
        print(f'Your answer: {answer}')

        if number % 2 == 0:
            right_answer = 'yes'

        else:
            right_answer = 'no'    
        
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
    even(user)   