import random
import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mult_inverse(e, phi_n):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi_n

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi_n


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

    phi_n = (p - 1) * (q - 1)

    e = random.randint(1, phi_n)

    g = gcd(e, phi_n)
    while g != 1:
        e = random.randrange(1, phi_n)
        g = gcd(e, phi_n)

    d = mult_inverse(e, phi_n)

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    e, n = pk

    cipher = [pow(ord(char), e, n) for char in plaintext]

    return cipher


def decrypt(pk, ciphertext):
    d, n = pk

    aux = [str(pow(char, d, n)) for char in ciphertext]

    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


def main():
    l = 100
    u = 1000

    p, q = choose_prime(l, u)
    public_key, private_key = generate_key_pair(p, q)

    message = input("Enter message: ")

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    print("Generating public / private key pair ...")
    main()
