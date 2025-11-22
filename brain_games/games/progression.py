from brain_games.utils import progression_maker, random_number


def progression():

    prog = progression_maker()
    muted_step = random_number(0, 9)
    right_answer = prog[muted_step]
    prog_to_show = prog[:]
    prog_to_show[muted_step] = '..' 
    question = f"Question: {' '.join(str(x) for x in prog)}"
    
    return right_answer, question