from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.even import even


def main():
    user = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine(user, even)    