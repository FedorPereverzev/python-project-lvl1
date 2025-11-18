import random


def random_number(start=0, end=100):
    return random.randint(start, end)


def random_operation():
    operations = ['+', '-']
    return operations[random_number(0, 1)]

