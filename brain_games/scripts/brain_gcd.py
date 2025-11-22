from brain_games.cli import welcome_user
from brain_games.engine import engine
from brain_games.games.gcd import gcd


def main():
    user = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    engine(user, gcd)





        


