from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.progression import progression


def main():
    user = welcome_user()
    print("What number is missing in the progression?")
    engine(user, progression)

