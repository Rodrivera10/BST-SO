import random


def generate_random(n):
    return random.sample(range(1, n * 10 + 1), n)


def generate_sorted(n):
    return list(range(1, n + 1))
