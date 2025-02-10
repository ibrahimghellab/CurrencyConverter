import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Liste des pays
countries = [
    "Oman", "Pakistan", "Palaos", "Panama", "Papouasie-Nouvelle-Guinée", "Portugal", "Porto Rico",
    "République Tchèque", "Slovaquie", "Slovénie", "Espagne", "France", "Italie", "Allemagne", "Royaume-Uni"
    # Ajoute ici tous les autres pays de la liste...
]

def open_country_window():
    # Désactiver le bouton principal
    button.config(state=tk.DISABLED)
    
    # Créer une nouvelle fenêtre
    country_window = tk.Toplevel(root)
    country_window.title("Sélectionner un pays")

    # Label
    search_label = tk.Label(country_window, text="Rechercher un pays:")
    search_label.pack(pady=5)

    # Combobox avec autocomplétion
    country_combobox = ttk.Combobox(country_window, values=countries, state="normal", width=30)
    country_combobox.pack(pady=5)

    # Bouton pour valider la sélection
    def select_country():
        selected_country = country_combobox.get()
        if selected_country in countries:
            label.config(text=f"Pays sélectionné: {selected_country}")
            country_window.destroy()
            button.config(state=tk.NORMAL)  # Réactiver le bouton de la fenêtre principale
        else:
            messagebox.showerror("Erreur", "Ce pays n'est pas dans la liste.")

    select_button = tk.Button(country_window, text="Sélectionner", command=select_country)
    select_button.pack(pady=10)

    # Fermer la fenêtre lorsque l'utilisateur ferme la fenêtre secondaire
    country_window.protocol("WM_DELETE_WINDOW", lambda: (country_window.destroy(), button.config(state=tk.NORMAL)))

# Fenêtre principale
root = tk.Tk()
root.title("Fenêtre Principale")

# Label pour afficher le pays sélectionné
label = tk.Label(root, text="Pays sélectionné: Aucun", font=("Arial", 14))
label.pack(pady=20)

# Bouton pour ouvrir la fenêtre de sélection de pays
button = tk.Button(root, text="Choisir un pays", command=open_country_window)
button.pack(pady=10)

root.mainloop()
