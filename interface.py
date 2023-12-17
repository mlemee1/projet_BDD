import customtkinter as ctk

from repertoire import Repertoire


class RepertoireUI(ctk.CTk):
    def __init__(self, repertoire: Repertoire):
        """
        Initialise l'interface utilisateur de l'application de répertoire.

        Args:
            repertoire (Repertoire): Instance de la classe Repertoire pour gérer les opérations de la base de données.
        """
        super().__init__()

        self.rep = repertoire

        self.init_ui()
        self.mainloop()

    def init_ui(self):
        """
        Configure l'interface utilisateur initiale, incluant la création et le placement des widgets.
        """
        self.title("Répertoire")
        self.geometry("400x350")
        ctk.set_appearance_mode("dark")

        ctk.CTkLabel(
            self, text="Répertoire", font=ctk.CTkFont(size=20, weight="bold")
        ).pack(padx=20, pady=(20, 0))

        ctk.CTkLabel(self, text="Bienvenue dans votre répertoire.").pack(
            padx=20, pady=10
        )

        for text, commande in [
            ("Ajouter un contact", self.ajout_contact),
            ("Afficher les contacts", self.afficher_contacts),
            ("Rechercher un contact", self.chercher_contacts),
            ("Supprimer un contact", self.supprimer_contact),
        ]:
            ctk.CTkButton(self, text=text, command=commande).pack(padx=20, pady=10)

        self.quitter_button(self).pack(padx=20, pady=10)

    def input_dialog(self, title: str, text: str) -> str:
        """
        Affiche une boîte de dialogue pour la saisie de l'utilisateur.

        Args:
            title (str): Le titre de la boîte de dialogue.
            text (str): Le texte à afficher dans la boîte de dialogue.

        Returns:
            str: La saisie de l'utilisateur.
        """
        dialog = ctk.CTkInputDialog(text=text, title=title)

        return dialog.get_input()

    def ajout_contact(self):
        """
        Gère l'ajout d'un nouveau contact. Ouvre des boîtes de dialogue pour saisir les informations du contact.
        """
        nom = self.input_dialog(
            "Nom de famille", "Entrez le nom de famille du contact :"
        )

        if not nom:
            return

        prenom = self.input_dialog("Prénom", "Entrez le prénom du contact :")

        if not prenom:
            return

        telephone = self.input_dialog(
            "Numéro de téléphone", "Entrez le numéro de téléphone du contact :"
        )

        if not telephone:
            return

        self.rep.ajouter_contact(nom, prenom, telephone)

    def afficher_contacts(self):
        """
        Affiche une nouvelle fenêtre listant tous les contacts stockés dans la base de données.
        """
        fenetre_contacts = ctk.CTkToplevel()
        fenetre_contacts.title("Affichage des contacts")
        fenetre_contacts.geometry("400x300")

        contacts = self.rep.afficher_contacts()

        if len(contacts) > 0:
            for contact in contacts:
                ctk.CTkLabel(
                    fenetre_contacts, text=f"{contact[0]} {contact[1]} : {contact[2]}"
                ).pack(padx=20, pady=1)
        else:
            ctk.CTkLabel(
                fenetre_contacts,
                text="Aucun contact n'est présent dans le répertoire !",
            ).pack(padx=20, pady=10)

        self.quitter_button(fenetre_contacts).pack(padx=20, pady=10)
        fenetre_contacts.after(100, fenetre_contacts.lift)

    def chercher_contacts(self):
        """
        Gère la recherche de contacts. Ouvre une boîte de dialogue pour la saisie du nom puis du prénom à rechercher.
        """
        nom = self.input_dialog("Nom du contact", "Entrez le nom du contact")

        if not nom:
            return

        prenom = self.input_dialog("Prénom du contact", "Entrez le prénom du contact")

        if not prenom:
            return

        fenetre_contacts = ctk.CTkToplevel()
        fenetre_contacts.title("Recherche de contacts")
        fenetre_contacts.geometry("400x300")

        ctk.CTkLabel(
            fenetre_contacts,
            text="Recherche de contacts",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(padx=20, pady=(20, 0))

        contacts = self.rep.chercher_contact(nom, prenom)

        if len(contacts) > 0:
            label_text = f"Nous avons trouvé {len(contacts)} contact(s) avec le nom '{nom} {prenom}'."
        else:
            label_text = (
                f"Nous n'avons pas trouvé de contact avec le nom '{nom} {prenom}'."
            )

        ctk.CTkLabel(fenetre_contacts, text=label_text).pack(padx=20, pady=10)

        for contact in contacts:
            ctk.CTkLabel(
                fenetre_contacts, text=f"{contact[0]} {contact[1]} : {contact[2]}"
            ).pack(padx=20, pady=1)

        self.quitter_button(fenetre_contacts).pack(padx=20, pady=10)

        fenetre_contacts.after(100, fenetre_contacts.lift)

    def supprimer_contact(self):
        """
        Gère la suppression d'un contact. Ouvre des boîtes de dialogue pour confirmer la suppression d'un contact spécifique.
        """
        nom = self.input_dialog(
            "Nom de famille", "Entrez le nom de famille du contact :"
        )

        if not nom:
            return

        prenom = self.input_dialog("Prénom", "Entrez le prénom du contact :")

        if not prenom:
            return

        fenetre_confirmation = ctk.CTkToplevel()
        fenetre_confirmation.title("Confirmation")
        fenetre_confirmation.geometry("400x300")

        ctk.CTkLabel(
            fenetre_confirmation,
            text="Suppression de contacts",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(padx=20, pady=(20, 0))

        ctk.CTkLabel(
            fenetre_confirmation,
            text="Êtes-vous certain(e) de vouloir supprimer ce contact ?",
        ).pack(padx=20, pady=10)

        ctk.CTkButton(
            fenetre_confirmation,
            text="Oui",
            command=lambda: self.confirmation_suppression(
                nom, prenom, fenetre_confirmation
            ),
        ).pack(padx=20, pady=10)

        ctk.CTkButton(
            fenetre_confirmation, text="Non", command=fenetre_confirmation.destroy
        ).pack(padx=20, pady=10)

    def confirmation_suppression(
        self, nom: str, prenom: str, fenetre_confirmation: ctk.CTkToplevel
    ):
        """
        Effectue la suppression effective d'un contact après confirmation de l'utilisateur.

        Args:
            nom (str): Le nom de famille du contact à supprimer.
            prenom (str): Le prénom du contact à supprimer.
            fenetre_confirmation (ctk.CTkToplevel): La fenêtre de confirmation de suppression.
        """
        fenetre_confirmation.destroy()

        fenetre_contacts = ctk.CTkToplevel()
        fenetre_contacts.title("Suppression de contacts")
        fenetre_contacts.geometry("400x300")

        ctk.CTkLabel(
            fenetre_contacts,
            text="Suppression de contacts",
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(padx=20, pady=(20, 0))

        suppression = self.rep.supprimer_contact(nom, prenom)

        if not suppression:
            label_text = f'Aucun contact "{prenom} {nom}" n\'a été trouvé.'
        else:
            label_text = f'Le contact "{prenom} {nom}" a bien été supprimé'

        ctk.CTkLabel(fenetre_contacts, text=label_text).pack(padx=20, pady=10)

        self.quitter_button(fenetre_contacts).pack(padx=20, pady=10)
        fenetre_contacts.after(100, fenetre_contacts.lift)

    def quitter_button(self, parent: ctk.CTk) -> ctk.CTkButton:
        """
        Crée un bouton 'Quitter' sur la fenêtre spécifiée.

        Args:
            parent (ctk.CTk): La fenêtre parente sur laquelle le bouton sera placé.

        Returns:
            ctk.CTkButton: Le bouton créé.
        """
        return ctk.CTkButton(parent, text="Quitter", command=parent.destroy)
