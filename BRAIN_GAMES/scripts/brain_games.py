#!/usr/bin/env python


from BRAIN_GAMES.cli import welcome_user, name


def ender(number):
    if number == 3:
        print(f'Congratulations, {name}')


def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
