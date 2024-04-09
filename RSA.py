import random

def is_prime(num):
    """ Vérifie si un nombre est premier """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keypair(p, q, e):
    """ Génère les clés publiques et privées pour RSA """
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Vérifier si e est premier avec phi
    if not is_prime(e) or e >= phi:
        raise ValueError("L'exposant de chiffrement e n'est pas valide")
    
    # Calculer l'inverse modulaire de e modulo phi
    d = pow(e, -1, phi)  # Utilisation de l'exponentiation modulaire pour calculer l'inverse
    
    # Retourner la clé publique (e, n) et la clé privée (d, n)
    return (e, n), (d, n)

def encrypt(message, public_key):
    """ Chiffre un message en utilisant la clé publique RSA """
    e, n = public_key
    ciphertext = pow(message, e, n)  # message^e mod n
    return ciphertext

def decrypt(ciphertext, private_key):
    """ Déchiffre un message chiffré en utilisant la clé privée RSA """
    d, n = private_key
    decrypted_message = pow(ciphertext, d, n)  # ciphertext^d mod n
    return decrypted_message

# Paramètres pour l'exemple
p = 5
q = 7
e = 5
message_original = 5

# Génération des clés publiques et privées
public_key, private_key = generate_keypair(p, q, e)
print("Clé publique (e, n) :", public_key)
print("Clé privée (d, n) :", private_key)

# Chiffrement du message original avec la clé publique
ciphertext = encrypt(message_original, public_key)
print("Message chiffré :", ciphertext)

# Déchiffrement du message chiffré avec la clé privée
decrypted_message = decrypt(ciphertext, private_key)
print("Message déchiffré :", decrypted_message)

# Vérification du déchiffrement
if decrypted_message == message_original:
    print("Déchiffrement réussi ! Le message déchiffré correspond au message original.")
else:
    print("Déchiffrement échoué ! Le message déchiffré ne correspond pas au message original.")
