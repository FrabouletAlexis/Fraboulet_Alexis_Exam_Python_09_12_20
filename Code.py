import random
from colorama import init 
init()
from colorama import Fore, Back, Style
def mot_aleatoire ():
    tableau_mot = ["retard","inouie","abbaye","clamer","dopant","alarme","ovuler","machin","enfler","alcool"]
    nb_mot=random.randrange(0,len(tableau_mot))
    for i in range (0,len(tableau_mot)):
        if (i == nb_mot):
            mot = tableau_mot[i]    
    return mot
def couleur (mot,mot_select):
    for i in range (0,len(mot_select)):
        if (mot[i] == mot_select[i]):
            print(Back.RED+ mot_select[i])
            print(Style.RESET_ALL) 
        elif (mot[i] != mot_select[i]):
            print(Back.BLUE+ mot_select[i])
            print(Style.RESET_ALL) 

# ------code------#
tentative=0
reussite=False   
mot=mot_aleatoire()

while (not(tentative == 9 or reussite == True)):
    
    if (tentative > 8):
        print ("Dommage le bon mot était", mot)
        
    mot_select=input("Votre proposition ?")
    if (mot == mot_select):
        print ("Félicitation vous avez trouvez le bon mot")
        reussite ==True
    else
        print (couleur(mot,mot_select))
        tentative = tentative +1
        print ("il vous reste", 8-tentative,"tentative")
    
    
    
input()