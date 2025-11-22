def engine(user_name, game):

    count_of_corrects = 0

    while count_of_corrects < 3:

        right_answer, question = game()
        
        print(question)
        
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