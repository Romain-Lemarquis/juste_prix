# -*- coding: utf-8 -*-
# 1) -  Importation des modules nécessaires
import random
import tkinter as tk
from tkinter import ttk

root = tk.Tk() 
root.geometry('300x200')

def action(event):
    
    # Obtenir l'élément sélectionné
    select = listeCombo.get()
    print("Vous avez sélectionné : '", select,"'")
    if select == "Débutant":
        Vie = 50
        print("vous avez 50 vies")
    if select == "Intermédiaire":
        Vie = 25
        print("vous avez 25 vies")
    if select == "Difficile":
        Vie = 10
        print("vous avez 10 vies")
    if select == "Légendaire":
        Vie = 5
        print("vous avez 5 vies")
    justePrix = random.randint(1,100)

    # Autre façon de faire
    # Exemple 1 :
    """
    options = {
    "Débutant": 50,
    "Intermédiaire": 25,
    "Difficile": 10,
    "Légendaire": 5
    }

    if select in options:
            Vie = options[select]
        print(f"vous avez {Vie} vies")
    else:
        print("Option non valide")
    """

    

    fin_du_jeu=False
    while(fin_du_jeu==False):
        if(Vie == 0):
            print("tu as perdu!")
            fin_du_jeu=True    
        print("Entrer le prix souhaité:")
        x = input()
        y= int (x)
        if(y > justePrix):
            print("la valeur écrite est supérieure au juste prix")
            Vie = Vie - 1
            print("il vous reste",Vie, "vie(s)")
        elif(y< justePrix):
            print("la valeur écrite est inférieure au juste prix")
            Vie = Vie - 1
            print("il vous reste",Vie, "vie(s)")
        else:
            print("tu as gagné!")
            fin_du_jeu=True
        

    labelChoix = tk.Label(root, text = "Veuillez faire un choix !")
    labelChoix.pack()

# 2) - créer la liste Python contenant les éléments de la liste Combobox
listeNiveaux=["Débutant", "Intermédiaire","Difficile","Légendaire"]

# 3) - Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(root, values=listeNiveaux)
 
# 4) - Choisir l'élément qui s'affiche par défaut
listeCombo.current(0)

listeCombo.pack()
listeCombo.bind("<<ComboboxSelected>>", action)

root.mainloop()
