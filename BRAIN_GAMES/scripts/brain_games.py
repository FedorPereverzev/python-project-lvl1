#!/usr/bin/env python


from BRAIN_GAMES.cli import welcome_user


def _main():
    welcome_user()


def ender(number, user_name):
    if number == 3:
        print(f'Congratulations, {user_name}')


if __name__ == '__main__':
    _main()
