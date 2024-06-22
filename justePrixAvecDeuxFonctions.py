# -*- coding: utf-8 -*-
# 1) -  Importation des modules nécessaires
import random
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')

def obtenirVies(select):
    # Utiliser un dictionnaire 
    options = {
        "Débutant": 50,
        "Intermédiaire": 25,
        "Difficile": 10,
        "Légendaire": 5
    }
    
    return options.get(select, 0)  # On retourne 0 si l'option n'est pas valide

def jouerJustePrix(vies, juste_prix):
    fin_du_jeu = False
    while not fin_du_jeu:
        if vies == 0:
            print("tu as perdu!")
            fin_du_jeu = True    
        else:
            print("Entrer le prix souhaité:")
            x = input()
            y = int(x)
            if y > juste_prix:
                print("la valeur écrite est supérieure au juste prix")
                vies -= 1
                print("il vous reste", vies, "vie(s)")
            elif y < juste_prix:
                print("la valeur écrite est inférieure au juste prix")
                vies -= 1
                print("il vous reste", vies, "vie(s)")
            else:
                print("tu as gagné!")
                fin_du_jeu = True

def action(event):
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    print("Vous avez sélectionné :", select)
    
    vies = obtenirVies(select)
    if vies == 0:
        print("Option non valide")
        return
    
    print(f"vous avez {vies} vies")
    juste_prix = random.randint(1, 100)

    jouerJustePrix(vies, juste_prix)

    labelChoix = tk.Label(root, text="Veuillez faire un choix !")
    labelChoix.pack()

# 2) - créer la liste Python contenant les éléments de la liste Combobox
listeNiveaux = ["Débutant", "Intermédiaire", "Difficile", "Légendaire"]

# 3) - Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(root, values=listeNiveaux)

# 4) - Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)

listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>", action)

root.mainloop()
