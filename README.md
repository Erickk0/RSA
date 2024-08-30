RSA Encryption and Decryption Implementation

This project is a Python-based implementation of the RSA (Rivest-Shamir-Adleman) encryption algorithm, one of the most widely used methods for secure data transmission. The RSA algorithm is a public-key cryptosystem that uses two keys—a public key for encryption and a private key for decryption. This project provides a clear and educational demonstration of how RSA works, including key generation, encryption, and decryption processes.
Features

    1. Prime Number Generation: Efficient algorithms to generate large prime numbers within a specified range.
    2. Key Pair Generation: Functionality to generate public and private keys based on selected prime numbers.
    3. Encryption: Ability to encrypt plaintext messages using the generated public key.
    4. Decryption: Ability to decrypt ciphertext back into plaintext using the corresponding private key.
    5. Mathematical Utilities: Includes functions for computing the greatest common divisor (GCD) and modular multiplicative inverses, which are crucial for the RSA algorithm.
    6. User Interaction: The main program prompts the user for a message, then encrypts and decrypts it, showcasing the RSA process in action.

How It Works

    1. Prime Number Selection: The program selects two large prime numbers from a user-defined range.
    2. Key Generation: Using the selected primes, the program calculates the modulus n and Euler's totient φ(n), then generates the public key e and private key d.
    3. Encryption: The user's plaintext message is encrypted using the public key, resulting in a series of numbers representing the encrypted message.
    4. Decryption: The encrypted message is decrypted using the private key, restoring the original plaintext message.

Use Cases

    1. Educational Tool: Ideal for students and educators looking to understand the RSA algorithm and public-key cryptography.
    2. Secure Communication: Can be adapted for basic secure messaging between parties, demonstrating the principles of public-key encryption.

Getting Started

To get started with this project:

    1. Clone the repository:

        git clone https://github.com/Erickk0/RSA_Simple.git

     2. Navigate to the project directory:

        cd RSA

     3. Run the Python script:

        python rsa.py
