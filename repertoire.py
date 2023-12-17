import sqlite3

from interface import RepertoireUI


class Repertoire:
    def __init__(self):
        """
        Initialise la classe Repertoire en établissant une connexion à la base de données SQLite.
        Prépare un curseur pour les opérations de base de données et initialise la structure de la base de données.
        """
        self.conn = sqlite3.connect("contacts.sqlite")
        self.cur = self.conn.cursor()

        self.setup_database()

    def setup_database(self):
        """
        Crée la table 'contacts' dans la base de données si elle n'existe pas déjà.
        Cette table est utilisée pour stocker les informations des contacts.
        """
        operation = """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                nom TEXT,
                prenom TEXT,
                telephone TEXT
            )
        """

        self.cur.execute(operation)

    def run(self):
        """
        Lance l'interface utilisateur de l'application de répertoire et assure une sortie propre en appelant 'exit'.
        """
        try:
            RepertoireUI(self)
        finally:
            self.exit()

    def exit(self):
        """
        Ferme le curseur et la connexion à la base de données pour une fermeture propre des ressources de la base de données.
        """
        self.cur.close()
        self.conn.close()

    def ajouter_contact(self, nom: str, prenom: str, telephone: str):
        """
        Ajoute un nouveau contact à la base de données.

        Args:
            nom (str): Le nom de famille du contact.
            prenom (str): Le prénom du contact.
            telephone (str): Le numéro de téléphone du contact.
        """
        self.cur.execute(
            "INSERT INTO contacts (nom, prenom, telephone) VALUES (?, ?, ?)",
            [nom, prenom, telephone],
        )

        self.conn.commit()

    def supprimer_contact(self, nom: str, prenom: str) -> bool:
        """
        Supprime un contact existant de la base de données en fonction de son nom et prénom.

        Args:
            nom (str): Le nom de famille du contact à supprimer.
            prenom (str): Le prénom du contact à supprimer.

        Returns:
            bool: True si le contact a été supprimé, False si aucun contact correspondant n'a été trouvé.
        """
        self.cur.execute(
            "SELECT id FROM contacts WHERE nom LIKE ? AND prenom LIKE ?",
            [f"%{nom}%", f"%{prenom}%"],
        )

        contact = self.cur.fetchone()

        if not contact:
            return False

        self.cur.execute("DELETE FROM contacts WHERE id = ?", [contact[0]])
        self.conn.commit()

        return True

    def afficher_contacts(self) -> list[tuple]:
        """
        Récupère et retourne tous les contacts de la base de données, triés par nom puis par prénom.

        Returns:
            list[tuple]: Liste de tuples, chaque tuple contenant les informations d'un contact (nom, prenom, telephone).
        """
        self.cur.execute(
            "SELECT nom, prenom, telephone FROM contacts ORDER BY nom, prenom"
        )

        return self.cur.fetchall()

    def chercher_contact(self, nom: str, prenom: str) -> list[tuple]:
        """
        Recherche des contacts dans la base de données par nom et prénom.

        Args:
            nom (str): Le nom à rechercher dans la base de données.
            prenom (str): Le prénom à rechercher dans la base de données.

        Returns:
            list of tuples: Liste de tuples des contacts correspondants, chaque tuple contenant les informations (nom, prenom, telephone).
        """
        self.cur.execute(
            "SELECT nom, prenom, telephone FROM contacts WHERE nom LIKE ? AND prenom LIKE ?",
            [f"%{nom}%", f"%{prenom}%"],
        )

        return self.cur.fetchall()
