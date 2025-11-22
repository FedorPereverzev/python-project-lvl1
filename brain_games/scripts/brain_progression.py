from brain_games.cli import welcome_user
from brain_games.utils import progression_maker, random_number


def progression(user_name):

    count_of_corrects = 0

    print("What number is missing in the progression?")
    
    while count_of_corrects < 3:

        prog = progression_maker()
        muted_step = random_number(0, 9)
        right_answer = prog[muted_step]
        prog_to_show = prog[:]
        prog_to_show[muted_step] = '..' 
        print(" ".join(str(x) for x in prog_to_show))

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
    progression(user)

