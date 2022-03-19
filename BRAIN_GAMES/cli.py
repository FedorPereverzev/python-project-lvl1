import prompt


name = prompt.string('May I have your name? ')


def welcome_user():
    print(f"Hello, {name}!")
