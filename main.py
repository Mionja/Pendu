from fonctions import *

def start():
    chance = 10
    list_mot_user = []
    the_list = []
    mot_user = ""
    mot = mot_complet()
    #print(mot)
    print("\nLe mot en complet est: {} \t (Vous avez {} chances)".format(mot_masque(mot, '*'), chance))
    print()
    while chance > 0:
        print()
        user_choice = lettre_a_recupere_de_l_utilisateur()
        if user_choice in list(mot):
            if user_choice not in list_mot_user:
                print("Bravo, {} est dans le mot que vous chercher".format(user_choice))
                list_mot_user.append(user_choice)
            elif user_choice in list_mot_user:
                print("Vous avez déjà choisit cette lettre")
            #print(list_mot_user)
            mot_user = mot_masque(mot, list_mot_user)
            print("\t ==>", mot_user)
            print("\tIl vous reste", chance, "chance(s)")
            #chance -= 1
        elif user_choice in the_list:
            print("Vous avez déjà choisit cette lettre et c'estait fausse")
        else:
            print("{} n'est pas dans le mot que vous devez trouvé".format(user_choice))
            the_list.append(user_choice)
            chance -= 1
            print("\tIl vous reste", chance, "chance(s)")
        if mot_user == mot:
            print("===========Felicitation, vous avez trouvé le mot\t votre score est de ", chance, "/10============")
            break
    if mot_user != mot:
        print("--------Vous avez perdu, le mot etait", mot,"---------")
    return chance


def reesayer():
    retry = input("Voulez vous quitter? (entrez Q pour quitter) : ")
    retry = retry.lower()
    if retry != "q":
       score()
    else:
        print("------thanks for playing------")


def salut(num):
    username = ""
    print("\nBienvenu à l'utilisateur n°: ", num)
    while username == "":
        username = input("Entrer votre nom : ")
    return username


def score():
    user1 = salut(1)
    score1 = start()
    user2 = salut(2)
    score2 = start()
    if score1 > score2:
        print("\n \t====================>>>>>>>", user1, " a gagné\n")
    elif score2 > score1:
        print("\n \t====================>>>>>>>", user2, " a gagné\n")
    else:
        print("\n \t====================>>>>>>>", "Egalité avec un score de ", score2, "\n")
    reesayer()


score()

