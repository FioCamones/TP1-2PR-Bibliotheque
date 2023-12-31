import random
import csv


#   NOUS AVONS COMME OBJECTIF DE CRÉER UN CODE LOGIQUE POUR UNE BIBLIOTHEQUE.
#   LA PREMIERE PARTIE CONSISTE À CRÉER NOS CLASSES
class Document:
    def __init__(self, titre):
        self.titre = titre


class Livre(Document):
    def __init__(self, titre, auteur, ISBN):
        super().__init__(titre)
        self.auteur = auteur
        self.isbn = ISBN


class BandeDessinee(Document):
    def __init__(self, titre, dessinateur):
        super().__init__(titre)
        self.dessinateur = dessinateur


class Dictionnaire(Document):
    def __init__(self, titre):
        super().__init__(titre)


class Journal(Document):
    def __init__(self, titre, date_parution):
        super().__init__(titre)
        self.date_parution = date_parution


class Adherent:
    def __init__(self, nom, prenom, age, num_adh):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.numadh = num_adh


class Emprunt:
    def __init__(self, nom_adherent, prenom_adherent, livre):
        self.nom = nom_adherent
        self.prenom = prenom_adherent
        self.livre = livre


class Bibliotheque:
    def __init__(self):
        self.adherents = []
        self.documents = []
        self.emprunts = []

    def ajouter_adherent(self, adherent):
        self.adherents.append(adherent)
        #

    def sauvegarde_adherent(self, nomFichier):
        # lire depuis fichier
        f = open(nomFichier, 'w')

        for adherent in self.adherents:
            print(adherent.nom + " " + adherent.prenom + " " + adherent.age + " " + adherent.numadh)
            f.write(adherent.nom + "," + adherent.prenom + "," + adherent.age + "," + adherent.numadh + "\n")
        f.close()
        nomfichier = "./fichier_adh.txt"
        # sauvegardeAdherent(nomfichier)

    def supprimer_adherent(self, nom, prenom):
        for adherent in self.adherents:
            if adherent.nom == nom and adherent.prenom == prenom:
                self.adherents.remove(adherent)
                print(f"{nom} {prenom} a été supprimé de la liste des adhérents.")
                return

        print(f"{nom} {prenom} n'est pas trouvé parmi les adhérents.")

    def afficher_adherents(self):
        print("Liste des adhérents :")
        for adherent in self.adherents:
            print(f"nom:{adherent.nom} prenom:{adherent.prenom} age:{adherent.age} numero d'adhérant:{adherent.numadh}")

    def ajouter_document(self, document):
        self.documents.append(document)

    def sauvegarder_doc(self, titre_livre):
        # lire depuis fichier
        l = open(titre_livre, 'w')

        for x in self.documents:
            print(x.titre + " " + x.auteur + " " + x.isbn)
            l.write(x.titre + "," + x.auteur + "," + x.isbn + "\n")
        l.close()
        nomfichier2 = "./fichier_document.txt"

    def charger_adh_depuis_fichier(self, nomFichierAdh):
        f = open(nomFichierAdh, 'r')
        lecture = csv.reader(f, delimiter=',')
        for x in lecture:
            #print(x)
            obj = Adherent(x[0], x[1], x[2], x[3])
            self.adherents.append(obj)
        f.close()

    def charger_doc_depuis_fichier(self, nomFichierdoc):
        f = open(nomFichierdoc, 'r')
        lecture = csv.reader(f, delimiter=',')
        for x in lecture:
            #print(x)
            docs = Livre(x[0], x[1], x[2])
            self.documents.append(docs)
        f.close()

    def supprimer_document(self, nom_doc):
        for document in self.documents:
            if document.titre == nom_doc:
                self.documents.remove(document)
                print(f"{nom_doc} a été supprimé de la liste des documents")
                return
            print(f"{nom_doc} n'est pas dans la liste de documents")

    def afficher_document(self):
        print("liste de documents :")
        for document in self.documents:
            print(f"titre:{document.titre}  auteur:{document.auteur}  ISBN:{document.isbn}")

    def ajouter_emprunt(self, emprunt):
        self.emprunts.append(emprunt)

    def afficher_emprunts(self):
        for emprunt in self.emprunts:
            nom_adherent = emprunt.nom
            prenom_adherent = emprunt.prenom
            titre_livre = emprunt.livre.titre
            print(f"{nom_adherent} {prenom_adherent} a emprunté {titre_livre}")

    def retour_emprunt(self, nom_adherent, prenom_adherent, titre_livre):
        for emprunt in self.emprunts:
            if emprunt.livre.titre == titre_livre and emprunt.nom == nom_adherent and emprunt.prenom == prenom_adherent:
                self.emprunts.remove(emprunt)
                print(f"{titre_livre} a été retourné par {nom_adherent} {prenom_adherent}")
                return

        print(f"Aucun emprunt correspondant trouvé.")


bibliotheque = Bibliotheque()
nomfichier = "./fichier_adh.txt"
nomfichier2 = "./fichier_document.txt"
while True:
    print("******************************************")
    print("*         Bienvenue à votre bibliothèque *")
    print("*                     Faites un choix :  *")
    print("******************************************")
    print("*    1       Ajouter adhérent            *")
    print("*    2       Supprimer adhérent          *")
    print("*    3       Afficher tous les adhérent  *")
    print("*    4       Ajouter Document            *")
    print("*    5       Supprimer Document          *")
    print("*    6       Afficher tous les Documents *")
    print("*    7       Ajouter Emprunts            *")
    print("*    8       Retour d’un Emprunts        *")
    print("*    9       Afficher tous les Emprunts  *")
    print("*    0       Sauvegarder Adh             *")
    print("*    L       Sauvegarde Livre            *")
    print("*    Q       Quitter                     *")
    print("******************************************")

    choix = input("Choisissez un option : ")
    #### Ajouter adhérent
    if choix == "1":
        nom = input("Nom de l'adhérent : ")
        prenom = input("Prénom de l'adhérent : ")
        age = input("Quel est votre âge : ")
        num_adh = str(random.randint(10000, 99999))
        adherent = Adherent(nom, prenom, age, num_adh)
        bibliotheque.ajouter_adherent(adherent)

    #### Supprimer un adhérent
    elif choix == "2":
        nom = input("Nom de l'adhérent à supprimer : ")
        prenom = input("Prénom de l'adhérent à supprimer : ")
        bibliotheque.supprimer_adherent(nom, prenom)

    #### Afficher tous les adhérents
    elif choix == "3":
        bibliotheque.charger_adh_depuis_fichier(nomfichier)
        bibliotheque.afficher_adherents()

    #### Ajouter un document
    elif choix == "4":
        type_document = input("Type de document (Livre, BandeDessinee, Dictionnaire, Journal) : ")
        titre_document = input("Titre du document : ")

        if type_document.lower() == "livre":
            auteur = input("Auteur du livre : ")
            isbn = str(random.randint(10000, 99999))
            document = Livre(titre_document, auteur, isbn)
        elif type_document.lower() == "bandedessinee":
            dessinateur = input("Dessinateur de la Bande Dessinée : ")
            document = BandeDessinee(titre_document, dessinateur)
        elif type_document.lower() == "dictionnaire":
            document = Dictionnaire(titre_document)
        elif type_document.lower() == "journal":
            date_parution = input("Date de parution du journal : ")
            document = Journal(titre_document, date_parution)
        else:
            print("Type de document non reconnu.")
            continue

        bibliotheque.ajouter_document(document)

    #### Supprimer Document
    elif choix == "5":
        titre_document = input("Titre du document à supprimer : ")
        bibliotheque.supprimer_document(titre_document)

    #### Afficher tous les Documents
    elif choix == "6":
        bibliotheque.charger_doc_depuis_fichier(nomfichier2)
        bibliotheque.afficher_document()

    #### Ajouter Emprunts
    elif choix == "7":
        nom_adherent = input("Nom de l'adhérent emprunteur : ")
        prenom_adherent = input("Prénom de l'adhérent emprunteur : ")
        titre_livre = input("Titre du livre emprunté : ")
        auteur_livre = input("Auteur du livre : ")
        emprunt = Emprunt(nom_adherent, prenom_adherent, Livre(titre_livre, auteur_livre))

        bibliotheque.ajouter_emprunt(emprunt)

    #### Retour d'un Emprunts
    elif choix == "8":
        nom_user = input("Nom de l'adhérent emprunteur : ")
        prenom_user = input("Prénom de l'adhérent emprunteur : ")
        title_livre = input("Titre du livre retourné : ")

        bibliotheque.retour_emprunt(nom_adherent, prenom_adherent, titre_livre)

    #### Afficher tous les Emprunts
    elif choix == "9":
        bibliotheque.afficher_emprunts()
    elif choix == "0":
        nomfichier = "./fichier_adh.txt"
        bibliotheque.sauvegarde_adherent(nomfichier)
    elif choix.upper() == "L":
        nomfichier2 = "./fichier_document.txt"
        bibliotheque.sauvegarder_doc(nomfichier2)

    elif choix == "Q":
        print("Au revoir!")
        break
    else:
        print("Choix erroné!")
