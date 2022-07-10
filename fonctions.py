from donnees import *
from random import choice
# import os
# import pickle
#
# os.chdir('D:\\Etude\\Python\\Pendu')
# with open('score_of_users.txt', 'w') as score:
#     score.write("")
# my_array ={}
#
# def save_user_score(user_name, user_score):
#     global my_array
#     with open('score_of_users.txt', 'rb') as recup:
#         Bscore = recup.read()
#         if user_name not in Bscore:
#             my_array += {user_name: user_score}
#             with open('score_of_users.txt', 'ab') as Ascore:
#                 my_pickler = pickle.Pickler(Ascore)
#                 my_pickler.dump(my_array)
#
#
# def register_or_recuperation_of_user_score(user_name):
#     with open('score_of_users.txt', 'rb') as recup:
#         Bscore = recup.read()
#         if user_name in Bscore:
#             my_unpickler = pickle.Unpickler(recup)
#             my_unpickler.load()
#         else:
#             save_user_score(user_name, 0)


def lettre_a_recupere_de_l_utilisateur():
    choix = ""
    while choix == "":
        choix = input("Entrez une lettre: ")
        if len(choix) > 1 or not choix.isalpha():
            print("-----ERREUR, Ce que vous avez entrer est invalide------\n")
            choix = ""
    choix = choix.lower()
    return choix


def mot_complet():
    mot = choice(liste_mots)
    return mot


def mot_masque(motComplet, lettreRecupere):
    masque = ""
    for lettre in motComplet:
        if lettre in lettreRecupere:
                masque += lettre
        else:
            masque += "*"
    return masque







