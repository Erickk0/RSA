import random
import math


def is_prime(n):
    if n <= 1:
        return False
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 2, 2):
        if n % i == 0:
            return False
    return True


def choose_prime(l, u):
    primes = [num for num in range(l, u + 1) if is_prime(num)]

    if len(primes) < 2:
        raise ValueError("Not enough prime numbers in the specified range.")

    p, q = random.sample(primes, 2)
    if p > q:
        p, q = q, p
    return p, q


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime")
    elif (p == q):
        raise ValueError("Prime numbers cannot be the same")

    n = p * q
    phi_n = (p-1)*(q-1)






'''
l, u = 100, 10000
p, q = choose_prime(l, u)
n = generate_key_pair(p,q)
print(f"Chosen primes: p = {p}, q = {q}, N = {n}")
n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number") 
'''
