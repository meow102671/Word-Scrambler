from sympy import gcd
from random import randint
import time

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
    time.sleep(0.4)
    
    if choice.lower() == "e":
        
        message = input("Enter a message for encryption: ")
        enc_mes, key = encryption(message)
        time.sleep(0.4)
        print(f"Your encrypted message: {enc_mes}")
        time.sleep(0.4)
        
    elif choice.lower() == "d":
        
        have_key = input("Do you have an encryption key? (Y)es (N)o \n")
        time.sleep(0.4)
        
        if have_key.lower() == "y":
            
            key = input("Enter your key: ")
            time.sleep(0.4)
            enc_mes = input("Enter your message: ")
            dec_mes = decryption(enc_mes, key)
            time.sleep(0.4)
            print(f"Your decrypted message: {dec_mes}")
            time.sleep(0.4)
            
        else:
            
            try:
                
                message = input("Enter a message for decryption: ")
                dec_mes = decryption(enc_mes, key)
                time.sleep(0.4)
                print(f"Your decrypted message: {dec_mes}")
                time.sleep(0.4)
                
            except NameError:
            
                print("No message to decrypt!!")
                time.sleep(0.4)
                
    elif choice.lower() == "q":
        
        print(f"Your encryption key is: {key}")
        quit()
        
    else:
        
        print("INVALID CHOICE")
        time.sleep(0.4)


