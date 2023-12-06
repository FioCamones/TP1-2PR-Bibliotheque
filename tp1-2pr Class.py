#   NOUS AVONS COMME OBJECTIF DE CRÉER UN CODE LOGIQUE POUR UNE BIBLIOTHEQUE.
#   LA PREMIERE PARTIE CONSISTE À CRÉER NOS CLASSES
class Document:
    def __init__(self, titre):
        self.titre = titre

class Livre(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur
        self.disponible = True

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
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Emprunt:
    def __init__(self, nom_adherent, prenom_adherent, livre, date_emprunt):
        self.nom = nom_adherent
        self.prenom = prenom_adherent
        self.livre = livre
        self.date_emprunt = date_emprunt
        #self.date_retour = None

class Bibliotheque:
    def __init__(self):
        self.adherents = []
        self.documents = []
        self.emprunts = []

    def ajouter_adherent(self, adherent):
        self.adherents.append(adherent)

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
            print(f"{adherent.nom} {adherent.prenom}")

    def ajouter_document(self, document):
        self.documents.append(document)

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
            print(f"{document.titre}")

    def ajouter_emprunt(self, emprunt):
        self.emprunts.append(emprunt)

    def afficher_emprunts(self):
        for emprunt in self.emprunts:
            print(f"{nom_adherent} {prenom_adherent} a emprunté {titre_livre}")

    def retour_emprunt(self, titre_livre, nom_adherent, prenom_adherent):
        for emprunt in self.emprunts:
            if emprunt.livre == titre_livre:
                self.emprunts.remove(emprunt)
                print(f"{titre_livre} a été retourné par{nom_adherent} {prenom_adherent}")


# Créez une instance de la bibliothèque
bibliotheque = Bibliotheque()

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
    print("*    0      Quitter                      *")
    print("******************************************")

    choix = input("Choisissez un option : ")

    if choix == "1":
        # Ajouter adhérent
        nom = input("Nom de l'adhérent : ")
        prenom = input("Prénom de l'adhérent : ")
        adherent = Adherent(nom, prenom)
        bibliotheque.ajouter_adherent(adherent)

    elif choix == "2":
        # Supprimer adhérent
        nom = input("Nom de l'adhérent à supprimer : ")
        prenom = input("Prénom de l'adhérent à supprimer : ")
        bibliotheque.supprimer_adherent(nom, prenom)

    elif choix == "3":
        # Afficher tous les adhérents
        bibliotheque.afficher_adherents()

    elif choix == "4":
        # Ajouter Document
        type_document = input("Type de document (Livre, BandeDessinee, Dictionnaire, Journal) : ")
        titre_document = input("Titre du document : ")

        if type_document.lower() == "livre":
            auteur = input("Auteur du livre : ")
            document = Livre(titre_document, auteur)
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
            continue  # Revenir au début de la boucle

        bibliotheque.ajouter_document(document)

    elif choix == "5":
        # Supprimer Document
        titre_document = input("Titre du document à supprimer : ")
        bibliotheque.supprimer_document(titre_document)

    elif choix == "6":
        # Afficher tous les Documents
        bibliotheque.afficher_document()

    elif choix == "7":
        # Ajouter Emprunts
        nom_adherent = input("Nom de l'adhérent emprunteur : ")
        prenom_adherent = input("Prénom de l'adhérent emprunteur : ")
        titre_livre = input("Titre du livre emprunté : ")
        emprunt = (nom_adherent, prenom_adherent , titre_livre)
        #date_emprunt = input("Date d'emprunt (YYYY-MM-DD) : ")

        bibliotheque.ajouter_emprunt(emprunt)

    elif choix == "8":
        # Retour d’un Emprunts
        nom_adherent = input("Nom de l'adhérent emprunteur : ")
        prenom_adherent = input("Prénom de l'adhérent emprunteur : ")
        titre_livre = input("Titre du livre retourné : ")
        #date_retour = input("Date de retour (YYYY-MM-DD) : ")

        bibliotheque.retour_emprunt(nom_adherent, prenom_adherent, titre_livre)

    elif choix == "9":
        # Afficher tous les Emprunts
        bibliotheque.afficher_emprunts()

    else:
        print("Choix erroné!")

    #elif choix == "0":
   # print("Au revoir!")
    #break

    #else:
        print("Choix erroné!")



