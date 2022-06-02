from random import randint
from os import system

def morpion_2_0():

  print(" ")
  print(" ")
  print("                                    ███╗░░░███╗░█████╗░██████╗░██████╗░██╗░█████╗░███╗░░██╗")
  print("                                    ████╗░████║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗░██║")
  print("                                    ██╔████╔██║██║░░██║██████╔╝██████╔╝██║██║░░██║██╔██╗██║")
  print("                                    ██║╚██╔╝██║██║░░██║██╔══██╗██╔═══╝░██║██║░░██║██║╚████║")
  print("                                    ██║░╚═╝░██║╚█████╔╝██║░░██║██║░░░░░██║╚█████╔╝██║░╚███║")
  print("                                    ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝")
  print(" ")
  print("Voici les règles : Le but du jeu est d’aligner avant son adversaire 3 symboles identiques horizontalement, verticalement ou en diagonale.")
  print(" ")
  commencement_morpion()

def commencement_morpion():

  x = input("Voulez-vous commencer ? (oui ou non) : ")
  if x == "non":
    return fin_de_partie_morpion()
  elif x == "oui":
    choix_symbole1 = input("Joueur 1 , quel symbole choisissez vous : X ou O ? ")
    if choix_symbole1 == "O":
      choix_symbole2 = "X"
      print("Le joueur 1 sera donc les O et le joueur 2 sera les X . ")
    elif choix_symbole1 == "X":
      choix_symbole2 = "O"
      print("Le joueur 1 sera donc les X et le joueur 2 sera les O . ")
    elif choix_symbole1 != "X" and choix_symbole1 != "O":
      commencement_morpion()
  else:
    commencement_morpion()

  premier_tour_morpion(choix_symbole1,choix_symbole2)

def premier_tour_morpion(choix_symbole1,choix_symbole2):
  premier_tour = randint(0,1)

  if premier_tour == 1:
    print("C'est le joueur 1 qui commence . ")
    print(" ")
    cases = [
      ["_","_","_"],
      ["_","_","_"],
      ["_","_","_"]
    ]
    i = 0
    while i < 3:
      print(" ",cases[i])
      i += 1

    action1_morpion(cases,choix_symbole1,choix_symbole2)
  else:
    print("C'est le joueur 2 qui commence . ")
    print(" ")
    cases = [["_","_","_"],
            ["_","_","_"],
            ["_","_","_"]         
    ]
    i = 0
    while i < 3:
      print(" ",cases[i])
      i += 1
    
    action2_morpion(cases,choix_symbole1,choix_symbole2)

def action1_morpion(cases,choix_symbole1,choix_symbole2):
  print(" ")
  print("Tour du joueur 1")
  print(" ")
  X = int(input("Sur quelle ligne voulez-vous jouer ? "))
  Y = int(input("Sur quelle colonne voulez-vous jouer ? "))
  print(" ")
  if X < 0 or X > 3 or Y < 0 or Y > 3:
    print("Valeur incorrecte , réessayez .")
    action1_morpion(cases,choix_symbole1,choix_symbole2) 
  if cases[X-1][Y-1] == "_":
    cases[X-1][Y-1] = choix_symbole1
    _ = system('cls')
    print(" ")
    i = 0
    while i < 3:
      print(" ",cases[i])
      i += 1

    condition_morpion(cases,1,choix_symbole1,choix_symbole1,choix_symbole2)
  else:
    print("Vous ne pouvez pas jouer ici . Réessayer .")
    action1_morpion(cases,choix_symbole1,choix_symbole2)



def action2_morpion(cases,choix_symbole1,choix_symbole2):
  print(" ")
  print("Tour du joueur 2")
  print(" ")
  X = int(input("Sur quelle ligne voulez-vous jouer ? "))
  Y = int(input("Sur quelle colonne voulez-vous jouer ? "))
  print(" ")
  if X < 0 or X > 3 or Y < 0 or Y > 3:
    print("Valeur incorrecte , réessayez .")
    action2_morpion(cases,choix_symbole1,choix_symbole2) 
  if cases[X-1][Y-1] == "_":
    cases[X-1][Y-1] = choix_symbole2
    print(" ")
    _ = system('cls')
    print(" ")
    i = 0
    while i < 3:
      print(" ",cases[i])
      i += 1
    condition_morpion(cases,2,choix_symbole2,choix_symbole1,choix_symbole2)
  else:
    print("Vous ne pouvez pas jouer ici . Réessayer .")
    action2_morpion(cases,choix_symbole1,choix_symbole2)

  
def condition_morpion(cases,joueur,symbole,choix_symbole1,choix_symbole2):

# Victoire Horizontal

  if cases[0][0] == cases[0][1] and cases[0][0] == cases[0][2] and cases[0][0] == symbole:
    print(" ")
    print("Victoire du joueur ",joueur,)
    return fin_de_partie_morpion()
    
  elif cases[1][0] == cases[1][1] and cases[1][0] == cases[1][2] and cases[1][0] == symbole:
    print(" ")
    print("Victoire du joueur ",joueur,)
    return fin_de_partie_morpion()
  
  elif cases[2][0] == cases[2][1] and cases[2][0] == cases[2][2] and cases[2][0] == symbole :
    print(" ")
    print("Victoire du joueur ",joueur,)
    return fin_de_partie_morpion()
    

# Victoire Vertical

  elif cases[0][0] == cases[1][0] and cases[0][0] == cases[2][0] and cases[0][0] == symbole:
    print(" ")
    print("Victoire du joueur ",joueur,)
    return fin_de_partie_morpion()
    
  elif cases[0][1] == cases[1][1] and cases[0][1] == cases[2][1] and cases[0][1] == symbole:
    print(" ")
    print("Victoire du joueur ",joueur,)
    return fin_de_partie_morpion()
    
  elif cases[0][2] == cases[1][2] and cases[0][2] == cases[2][2] and cases[0][2] == symbole:
    print(" ")
    print("Victoire du joueur ",joueur,)
    return fin_de_partie_morpion()
   

# Victoire Diagonale
  
  elif cases[0][0] == cases[1][1] and cases[0][0] == cases[2][2] and cases[0][0] == symbole:
    print(" ")
    print("Victoire du joueur ",joueur,)
    return fin_de_partie_morpion()
   
  elif cases[0][2] == cases[1][1] and cases[0][2] == cases[2][0] and cases[0][2] == symbole:
    print(" ")
    print("Victoire du joueur ",joueur,)
    return fin_de_partie_morpion()


# Si match nul

  elif cases[0][0] != "_" and cases[0][1] != "_" and cases[0][2] != "_" and cases[1][0] != "_" and cases[1][1] != "_" and cases[1][2] != "_" and cases[2][0] != "_" and cases[2][1] != "_" and cases[2][2] != "_":
    print(" ")
    print("Match Nul .")
    return fin_de_partie_morpion()


# Si pas de coup décisif

  else:
    if joueur == 1:
      action2_morpion(cases,choix_symbole1,choix_symbole2)
    else:
      action1_morpion(cases,choix_symbole1,choix_symbole2)
  
def fin_de_partie_morpion():
  print("Partie terminée .")
  choix = input()


