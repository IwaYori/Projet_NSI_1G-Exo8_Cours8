from random import randint

allumettes = 21
allJoueur = 0
allOrdi = 0

while allumettes > 0:
   print("Il y a", allumettes, "allumettes.")
   
   allJoueur = int(input("Combien prenez-vous d'allumettes ? : "))
   allumettes = allumettes - allJoueur
   
   if allumettes >= 3:
      allOrdi = randint(1,3)
   elif allumettes == 2:
      allOrdi = randint(1,2)
   else:
      allOrdi = 1
      
   print("Je prends", allOrdi, "allumettes.")
   allumettes = allumettes - allOrdi