import csv
nomfichier = "./fichier_adh.txt"

fichier = open(nomfichier, 'r')
list_adh = []
lecture = csv.reader(fichier, delimiter=',')
for adherent in lecture:
    print(adherent)

fichier.close()

print("*****")
print(" ")

elif choix == "9":
    bibliotheque.afficher_emprunts()

elif choix == "0":
    print("Au revoir!")
    break
else:
    print("Choix erroné!")