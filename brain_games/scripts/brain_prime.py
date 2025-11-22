from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.prime import prime


def main():
    user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine(user, prime)