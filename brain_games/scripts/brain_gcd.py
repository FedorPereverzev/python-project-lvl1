from brain_games.cli import welcome_user
from brain_games.utils import is_gcd, random_number


def gcd(user_name):

    count_of_corrects = 0

    print("Find the greatest common divisor of given numbers.")
    
    while count_of_corrects < 3:

        number_1, number_2 = random_number(), random_number()

        print(f'Question: {number_1} {number_2}')

        right_answer = is_gcd(number_1, number_2)

        answer = input()
        print(f'Your answer: {answer}')

        if answer == str(right_answer):
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
    gcd(user)





        


