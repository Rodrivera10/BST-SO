import random

def generate_random(n):
    return [random.randint(1, 10000) for _ in range(n)]

def generate_sorted(n):
    return list(range(1, n + 1))