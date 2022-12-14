from random import randint
allumettes = 21
allJoueur = 0
allOrdi = 0

while allumettes > 0:
   print("Il y a", allumettes, "allumettes.")
   
   allJoueur = int(input("Combien prenez-vous d'allumettes ? : "))
   while allJoueur > 3 or allJoueur > allumettes: 
      allJoueur = int(input("Saisissez un nombre d'allumettes correct : "))
      
   
   allumettes = allumettes - allJoueur
   if allumettes == 0:
      print("\nVous avez perdu...")
      break
   
   if allumettes % 4 == 3:
      allOrdi = 2
   else:
      allOrdi = 1
      

   print("Je prends", allOrdi, "allumettes.")
   allumettes = allumettes - allOrdi
   if allumettes == 0:
      print("\nVous avez gagné ! :)")