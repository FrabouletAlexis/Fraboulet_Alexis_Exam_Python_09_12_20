
import random

def mot_aleatoire ():
    tableau_mot = ["RETARD","INOUIE","ABBAYE","CLAMER","DOPANT","ALARME","OVULER","MACHIN","ENFLER","ALCOOL"]
    nb_mot=random.randrange(0,len(tableau_mot))
    for i in range (0,len(tableau_mot)):
        if (i == nb_mot):
            mot = tableau_mot[i]    
    return mot
def analyse_mot_select (mot_select,mot):
    
    
mot= mot_aleatoire()

mot_select= int(input("Votre proposition ?"))

input()