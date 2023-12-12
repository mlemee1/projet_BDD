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
 
    def ajouter_contact(self, nom, prenom, telephone):
        # Ajout d'un nouveau contact
        self.cur.execute(
            "INSERT INTO contacts (nom, prenom, telephone) VALUES (?, ?, ?)",
            [nom, prenom, telephone],
        )
 
        self.conn.commit()
 
    def supprimer_contact(self, nom, prenom):
        # Suppression d'un contact existant
        self.cur.execute(
            "SELECT id FROM contacts WHERE nom = ? AND prenom = ?", [nom, prenom]
        )
 
        contact = self.cur.fetchone()
        if not contact:
            return False
 
 
        self.cur.execute("DELETE FROM contacts WHERE id = ?", [contact[0]])
        self.conn.commit()
 
        return True
 
    def afficher_contacts(self):
        # Affichage de tous les contacts
        self.cur.execute(
            "SELECT nom, prenom, telephone FROM contacts ORDER BY nom, prenom"
        )
 
        contacts = self.cur.fetchall()
 
        return contacts
 
    def chercher_contact(self, nom: str):
        # Recherche d'un contact
        self.cur.execute(
            "SELECT nom, prenom, telephone FROM contacts WHERE nom LIKE ? OR prenom LIKE ?",
            [f"%{nom}%", f"%{nom}%"],
        )
 
        resultats = self.cur.fetchall()
 
        return resultats
