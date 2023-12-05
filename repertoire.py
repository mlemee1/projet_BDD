import sqlite3


class Repertoire:
    def __init__(self):
        # Initialisation de la connexion à la base de données
        self.conn = sqlite3.connect("contacts.sqlite")
        self.cur = self.conn.cursor()
        self.setup_database()

    def setup_database(self):
        # Création de la table des contacts si elle n'existe pas
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                nom TEXT,
                prenom TEXT,
                telephone TEXT
            )
        """
        )
        self.conn.commit()

    def run(self):
        # Boucle principale du programme
        actions = {
            "1": self.ajouter_contact,
            "2": self.supprimer_contact,
            "3": self.afficher_contacts,
            "4": self.chercher_contact,
            "5": self.quitter,
        }

        while True:
            choix = input(
                "-----------------------------------------\n"
                "Que voulez-vous faire ?\n"
                "1 - Ajouter un contact\n"
                "2 - Supprimer un contact\n"
                "3 - Afficher tous les contacts\n"
                "4 - Chercher un contact\n"
                "5 - Quitter\n"
                "Choix : "
            )

            action = actions.get(choix)

            if action:
                action()
            else:
                print("Choix non valide.")

    def ajouter_contact(self):
        # Ajout d'un nouveau contact
        nom = input("Entrez le nom : ")
        prenom = input("Entrez le prénom : ")
        telephone = input("Entrez le numéro de téléphone : ")

        self.cur.execute(
            "INSERT INTO contacts (nom, prenom, telephone) VALUES (?, ?, ?)",
            [nom, prenom, telephone],
        )

        self.conn.commit()

        print("Contact ajouté avec succès.")

    def supprimer_contact(self):
        # Suppression d'un contact existant
        nom = input("Entrez le nom du contact à supprimer : ")
        prenom = input("Entrez le prénom du contact à supprimer : ")

        self.cur.execute(
            "SELECT id FROM contacts WHERE nom = ? AND prenom = ?", [nom, prenom]
        )

        contact = self.cur.fetchone()

        if contact:
            confirmation = input(
                "Êtes-vous sûr de vouloir supprimer ce contact ? (oui/non) : "
            )

            if confirmation.lower() == "oui":
                self.cur.execute("DELETE FROM contacts WHERE id = ?", [contact[0]])
                self.conn.commit()

                print("Contact supprimé.")
            else:
                print("Suppression annulée.")
        else:
            print("Contact non trouvé.")

    def afficher_contacts(self):
        # Affichage de tous les contacts
        self.cur.execute(
            "SELECT nom, prenom, telephone FROM contacts ORDER BY nom, prenom"
        )

        contacts = self.cur.fetchall()

        if contacts:
            for contact in contacts:
                print(
                    f"Nom: {contact[0]}, Prénom: {contact[1]}, Téléphone: {contact[2]}"
                )
        else:
            print("Aucun contact enregistré.")

    def chercher_contact(self):
        # Recherche d'un contact
        recherche = input("Entrez le nom ou le prénom à rechercher : ")

        self.cur.execute(
            "SELECT nom, prenom, telephone FROM contacts WHERE nom LIKE ? OR prenom LIKE ?",
            [f"%{recherche}%", f"%{recherche}%"],
        )

        resultats = self.cur.fetchall()

        if resultats:
            for contact in resultats:
                print(
                    f"Nom: {contact[0]}, Prénom: {contact[1]}, Téléphone: {contact[2]}"
                )
        else:
            print("Aucun contact correspondant trouvé.")

    def quitter(self):
        print("Au revoir !")
        exit()
