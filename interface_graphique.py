import customtkinter
 
from repertoire import Repertoire
 
app = customtkinter.CTk()
 
app.title("Répertoire")
 
app.geometry("400x350")
 
customtkinter.set_appearance_mode("dark")
 
rep = Repertoire()
 
 
def ajout_contact():
    input_nom = customtkinter.CTkInputDialog(text="Entrez le nom de famille du contact :", title="Nom de famille")
    nom = input_nom.get_input()
    if not nom:
        return
    input_prenom = customtkinter.CTkInputDialog(text="Entrez le prénom du contact :", title="Prénom")
    prenom = input_prenom.get_input()
    if not prenom:
        return
    input_telephone = customtkinter.CTkInputDialog(text="Entrez le numéro de téléphone du contact :", title="Numéro de téléphone")
    telephone = input_telephone.get_input()
 
    if not telephone:
        return
 
    rep.ajouter_contact(nom, prenom, telephone)

 
def afficher_contacts():
    fenetre_contacts = customtkinter.CTkToplevel()
    fenetre_contacts.title("Affichage des contacts")
    fenetre_contacts.geometry("400x300")
    contacts = rep.afficher_contacts()
    for contact in contacts:
        label = customtkinter.CTkLabel(fenetre_contacts, text=f"{contact[0]} {contact[1]} : {contact[2]}")
        label.pack(padx=20, pady=1)
    quitter(fenetre_contacts).pack(padx=20, pady=10)
    fenetre_contacts.after(100, fenetre_contacts.lift)

 
def chercher_contacts():
    input_nom = customtkinter.CTkInputDialog(text="Entrez le nom ou le prénom du contact", title="Nom du contact")
    nom = input_nom.get_input()
    if not nom:
        return
    fenetre_contacts = customtkinter.CTkToplevel()
    fenetre_contacts.title("Recherche de contacts")
    fenetre_contacts.geometry("400x300")
    titre = customtkinter.CTkLabel(fenetre_contacts, text="Recherche de contacts", font=customtkinter.CTkFont(size=20, weight="bold"))
    titre.pack(padx=20, pady=(20, 0))
    contacts = rep.chercher_contact(nom)
    if len(contacts) > 0:
        label = customtkinter.CTkLabel(fenetre_contacts, text=f"Nous avons trouvé {len(contacts)} contact(s) avec le nom {nom}.")
    else:
        label = customtkinter.CTkLabel(fenetre_contacts, text=f"Nous n'avons pas trouvé de contact avec le nom {nom}.")
    label.pack(padx=20, pady=10)
    for contact in contacts:
        label = customtkinter.CTkLabel(fenetre_contacts, text=f"{contact[0]} {contact[1]} ({contact[2]})")
        label.pack(padx=20, pady=1)
    quitter(fenetre_contacts).pack(padx=20, pady=10)
    fenetre_contacts.after(100, fenetre_contacts.lift)

 
def supprimer_contact():
    input_nom = customtkinter.CTkInputDialog(text="Entrez le nom de famille du contact :", title="Nom de famille")
    nom = input_nom.get_input()
    if not nom:
        return
    input_prenom = customtkinter.CTkInputDialog(text="Entrez le prénom du contact :", title="Prénom")
    prenom = input_prenom.get_input()
    if not prenom:
        return
    fenetre_confirmation = customtkinter.CTkToplevel().title("Confirmation").geometry("400x300")
    customtkinter.CTkLabel(fenetre_confirmation, text="Suppression de contacts", font=customtkinter.CTkFont(size=20, weight="bold")).pack(padx=20, pady=(20, 0))
    customtkinter.CTkLabel(fenetre_confirmation, text="Êtes-vous certain(e) de vouloir supprimer ce contact ?")
    customtkinter.CTkButton(fenetre_confirmation, text="Oui", command=afficher_contacts)
    customtkinter.CTkButton(fenetre_confirmation, text="Non", command=afficher_contacts)
 
    fenetre_contacts = customtkinter.CTkToplevel().title("Suppression de contacts").geometry("400x300")
    customtkinter.CTkLabel(fenetre_contacts, text="Suppression de contacts", font=customtkinter.CTkFont(size=20, weight="bold")).pack(padx=20, pady=(20, 0))
    suppression = rep.supprimer_contact(nom, prenom)
 
    if not suppression:
        label = customtkinter.CTkLabel(fenetre_contacts, text=f"Aucun contact \"{prenom} {nom}\" n'a été trouvé.")
    else:
        label = customtkinter.CTkLabel(fenetre_contacts, text=f"Le contact \"{prenom} {nom}\" a bien été supprimé")
 
    label.pack(padx=20, pady=10)
    quitter(fenetre_contacts).pack(padx=20, pady=10)
    fenetre_contacts.after(100, fenetre_contacts.lift)

 
def quitter(fenetre):
    return customtkinter.CTkButton(fenetre, text="Quitter", command=fenetre.destroy)

 
titre = customtkinter.CTkLabel(app, text="Répertoire", font=customtkinter.CTkFont(size=20, weight="bold"))
titre.pack(padx=20, pady=(20, 0))
 
label = customtkinter.CTkLabel(app, text="Bienvenue dans votre répertoire.")
label.pack(padx=20, pady=10)
 
ajout_contact_button = customtkinter.CTkButton(app, text="Ajouter un contact", command=ajout_contact)
ajout_contact_button.pack(padx=20, pady=10)
 
afficher_contacts_button = customtkinter.CTkButton(app, text="Afficher les contacts", command=afficher_contacts)
afficher_contacts_button.pack(padx=20, pady=10)
 
rechercher_contacts_button = customtkinter.CTkButton(app, text="Rechercher un contact", command=chercher_contacts)
rechercher_contacts_button.pack(padx=20, pady=10)
 
supprimer_contact_button = customtkinter.CTkButton(app, text="Supprimer un contact", command=supprimer_contact)
supprimer_contact_button.pack(padx=20, pady=10)
 
quitter(app).pack(padx=20, pady=10)
 
app.mainloop()