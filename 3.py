from random import randint
allumettes = 21
allJoueur = 0
allOrdi = 0

while allumettes > 0:
   print("Il y a", allumettes, "allumettes.")
   
   allJoueur = int(input("Combien prenez-vous d'allumettes ? : "))
   #assert allJoueur <= 3 and allJoueur < allumettes, "Veuillez respecter les conditions pour prendre des allumettes" -> méthode 1
   while allJoueur > 3 or allJoueur > allumettes: # -> méthode 2
      allJoueur = int(input("Saisissez un nombre d'allumettes correct : "))
      
   
   allumettes = allumettes - allJoueur
   if allumettes == 0:
      print("\nVous avez perdu...")
      break
   
   if allumettes >= 3:
      allOrdi = randint(1,3)
   elif allumettes == 2:
      allOrdi = randint(1,2)
   else:
      allOrdi = 1
      
   print("Je prends", allOrdi, "allumettes.")
   allumettes = allumettes - allOrdi
   if allumettes == 0:
      print("\nVous avez gagné ! :)")