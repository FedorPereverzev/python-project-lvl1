import random


def random_number(start=0, end=100):
    # noqa: S311
    return random.randint(start, end)


def random_operation():
    OPERATIONS = ['+', '-']
    return OPERATIONS[random_number(0, 1)]


def is_gcd(x, y):
    while y != 0:
        x, y = y, x % y 
    return x 


def progression_maker():
    start = random_number()
    step = random_number(1)
    coll = [start,]
    while len(coll) < 10:
        next_value = int(coll[-1]) + step
        coll.append(next_value)
    return coll


def is_prime(n):
    if n <= 1:
        return 'no'
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'no'
    
    return 'yes'