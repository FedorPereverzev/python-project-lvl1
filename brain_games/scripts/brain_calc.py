
from brain_games.cli import welcome_user
from brain_games.games.calc import calc


def main():
    user = welcome_user()
    print('What is the result of the expression?')
    calc(user, calc)   