from sympy import gcd
from random import randint

def find_valid_k(n):
    """Finds a k that is coprime with n."""
    k = randint(2, n - 1)  
    while gcd(k, n) != 1:  
        k = randint(2, n - 1)
    return k

def eqn(x, n, k):
    """Applies the permutation function."""
    return (x * k) % n

def eqn_inverse(y, n, k):
    """Finds the inverse mapping for decryption."""
    for i in range(n):
        if eqn(i, n, k) == y:
            return i 
    return None  

def encryption(message):
    """Encrypts the message using modular transformation."""
    n = len(message)
    k = find_valid_k(n)  
    encrypted_message = [""] * n

    for pos, char in enumerate(message):
        new_pos = eqn(pos, n, k)
        encrypted_message[new_pos] = char

    return "".join(encrypted_message), k  

def decryption(encrypted_message, k):
    """Decrypts the message using the inverse function."""
    n = len(encrypted_message)
    decrypted_message = [""] * n

    for pos, char in enumerate(encrypted_message):
        new_pos = eqn_inverse(pos, n, k)
        decrypted_message[new_pos] = char

    return "".join(decrypted_message)



while True:
    choice = input("Do you want to encrypt or decrypt a message, press (E) for encrypt (D) for decrypt, press (Q) for quit the program\n")
    if choice.lower() == "e":
        message = input("Enter a message for encryption: ")
        enc_mes, key = encryption(message)
        print(f"Your encrypted message: {enc_mes}")
    elif choice.lower() == "d":
        try:
            message = input("Enter a message for decryption: ")
            dec_mes = decryption(enc_mes, key)
            print(f"Your decrypted message: {dec_mes}")
        except NameError:
            print("No message to decrypt!!")
        
    elif choice.lower() == "q":
        quit()
    else:
        print("INVALID CHOICE")


