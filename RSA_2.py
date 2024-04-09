import random

def est_premier(num):
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

def generer_cle_publique_privee(p, q, e):
    """ Génère les clés publiques et privées pour RSA """
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Vérifier si e est premier avec phi
    if not est_premier(e) or e >= phi:
        raise ValueError("L'exposant de chiffrement e n'est pas valide")
    
    # Calculer l'inverse modulaire de e modulo phi pour obtenir d
    d = inverse_modulaire(e, phi)
    
    # Retourner la clé publique (e, n) et la clé privée (d, n)
    return (e, n), (d, n)

def chiffrer_bloc(message_bloc, cle_publique):
    """ Chiffre un bloc de message en utilisant la clé publique RSA """
    e, n = cle_publique
    message_chiffre_bloc = pow(message_bloc, e, n)  # message_bloc^e mod n
    return message_chiffre_bloc

def dechiffrer_bloc(message_chiffre_bloc, cle_privee):
    """ Déchiffre un bloc de message chiffré en utilisant la clé privée RSA """
    d, n = cle_privee
    message_dechiffre_bloc = pow(message_chiffre_bloc, d, n)  # message_chiffre_bloc^d mod n
    return message_dechiffre_bloc

def diviser_message(message, taille_bloc):
    """ Divise un message en blocs de la taille spécifiée """
    blocs = []
    for i in range(0, len(message), taille_bloc):
        blocs.append(int(message[i:i+taille_bloc]))
    return blocs

def combiner_blocs(blocs):
    """ Combine les blocs chiffrés en un seul message chiffré """
    message_chiffre = ""
    for bloc in blocs:
        message_chiffre += str(bloc) + " "
    return message_chiffre.strip()

def inverse_modulaire(a, m):
    """ Calcule l'inverse modulaire de a modulo m en utilisant l'algorithme d'Euclide étendu """
    _, d, _ = extended_gcd(a, m)
    if d < 0:
        d += m
    return d

def extended_gcd(a, b):
    """ Calcule le PGCD étendu de deux nombres et trouve les coefficients de Bézout """
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Paramètres pour l'exemple
p = 47
q = 71
e = 79
message_original = "6882326879666683"  # Message à chiffrer
taille_bloc = len(str(p * q)) - 1  # Taille maximale du bloc

# Génération des clés publiques et privées pour RSA
cle_publique, cle_privee = generer_cle_publique_privee(p, q, e)

# Division du message en blocs
blocs_message = diviser_message(message_original, taille_bloc)

# Chiffrement de chaque bloc de message
blocs_chiffres = []
for bloc in blocs_message:
    bloc_chiffre = chiffrer_bloc(bloc, cle_publique)
    blocs_chiffres.append(bloc_chiffre)

# Assemblage des blocs chiffrés en un seul message chiffré
message_chiffre_final = combiner_blocs(blocs_chiffres)
print("Message chiffré :", message_chiffre_final)

# Déchiffrement du message chiffré
blocs_dechiffres = []
for bloc_chiffre in blocs_chiffres:
    bloc_dechiffre = dechiffrer_bloc(bloc_chiffre, cle_privee)
    blocs_dechiffres.append(bloc_dechiffre)

# Reconstruction du message déchiffré à partir des blocs déchiffrés
message_dechiffre = ''.join(str(bloc) for bloc in blocs_dechiffres)
print("Message déchiffré :", message_dechiffre)
