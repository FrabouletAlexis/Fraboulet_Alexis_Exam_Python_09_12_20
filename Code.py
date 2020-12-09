import random
from colorama import init 
init()
from colorama import Fore, Back, Style
def mot_aleatoire ():
    tableau_mot = ["RETARD","INOUIE","ABBAYE","CLAMER","DOPANT","ALARME","OVULER","MACHIN","ENFLER","ALCOOL"]
    nb_mot=random.randrange(0,len(tableau_mot))
    for i in range (0,len(tableau_mot)):
        if (i == nb_mot):
            mot = tableau_mot[i]    
    return mot
def couleur (mot,mot_select):
    for i in range (0,len(mot_select)):
        if (mot[i] == mot_select[i]):
            print(Back.RED+ mot_select[i])
        elif (mot[i] != mot_select[i]):
            print(Back.BLUE+ mot_select[i])


# ------code------#
tentative=0
reussite=False   
mot=mot_aleatoire()

while (not(tentative == 9 or reussite == True)):

    mot_select=input("Votre proposition ?")
    print (couleur(mot,mot_select))
    if (





input()