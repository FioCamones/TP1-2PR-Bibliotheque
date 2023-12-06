import csv
nomfichier = "./fichier_adh.txt"
#lire depuis fichier
fichier = open(nomfichier, 'r')
list_adh = []
lecture = csv.reader(fichier, delimiter=',')
for adherent in lecture:
     print(adherent)
     list_adh.append(adherent)
fichier.close()


def sauvegardeAdherent(list_adh, nomfichier):
     # lire depuis fichier
     f = open(nomfichier, 'w')
     for x in list_adh:
          f.write(x[0] + "," + x[1] + "," + "\n")
     f.close()


# ecrire dans fichier
# liste adh, nom fichier
nomfichier = "./fichier_adh_test.txt"
sauvegardeAdherent(list_adh, nomfichier)

