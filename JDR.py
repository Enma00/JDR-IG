import random
import tkinter as tk

# Attaquer
def attaquer():
    global ENNEMI, HERO, SKIP
    
    if SKIP:
        text_box.insert(tk.END, "Vous passez votre tour\n")
        SKIP = False
    else: 
        Hit = random.randint(5,10)
        ENNEMI -= Hit
        text_box.insert(tk.END, f"Vous avez infligé {Hit} points de dégats ! \n")
        text_box.insert(tk.END, f"Il reste {ENNEMI} points de vie à ce mécréant !\n")
        
        if ENNEMI <= 0:
            text_box.insert(tk.END, " Tu as gagné !\n")
            attaquer_button.config(state="disabled")
            potion_button.config(state="disabled")
        else:
            Ennemi_hit = random.randint(5,15)
            HERO -= Ennemi_hit
            text_box.insert(tk.END, f"L'ennemi vous a infligé {Ennemi_hit} points de dégats ! \n")
            text_box.insert(tk.END, f"Il vous reste {HERO} points de vie.\n")
            if HERO <= 0:
                text_box.insert(tk.END, "Tu as perdu !\n")
                attaquer_button.config(state="disabled")
                potion_button.config(state="disabled")
            
    refresh_pv()
    text_box.see("end")


# Flask
def potion():
    global FLASK, HERO, SKIP
    
    if FLASK > 0:
        FLASK -= 1
        SKIP = True
        flask_use = random.randint(15,50)
        HERO += flask_use
        text_box.insert(tk.END, f"Vous avez récupéré {flask_use} PV ! \n")
        refresh_pv()
        text_box.see("end")

    else:
        text_box.insert(tk.END, "Vous n'avez plus de potion.\n")

# Maj points de vie
def refresh_pv():
    global HERO, ENNEMI
    
    hero_pv.config(text=f"Mes PV : {HERO}")
    ennemi_pv.config(text=f"PV ennemi : {ENNEMI}")

# Variables
ENNEMI = 50
HERO = 50
FLASK = 3
SKIP = False

def restart_game():
    global ENNEMI, HERO, FLASK, SKIP
    ENNEMI = 50
    HERO = 50
    FLASK = 3
    SKIP = False
    attaquer_button.config(state="normal")
    potion_button.config(state="normal")
    refresh_pv()
    text_box.delete("1.0", tk.END)

# Interface graphique
window = tk.Tk()
window.title("Jeu de combat")
window.geometry("500x500")

# Affichage PV
hero_pv = tk.Label(window, text=f"Mes PV : {HERO}")
hero_pv.pack()

ennemi_pv = tk.Label(window, text=f"PV ennemi : {ENNEMI}")
ennemi_pv.pack()

# Affichage dégats infligés
text_box = tk.Text(window)
text_box.pack()

# Barre de défilement
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)

# Boutons
attaquer_button = tk.Button(window, text="Attaquer", command=attaquer)
attaquer_button.pack(side=tk.LEFT, padx=10, pady=10)

potion_button = tk.Button(window, text="Potion", command=potion)
potion_button.pack(side=tk.LEFT, padx=10, pady=10)

recommencer_button = tk.Button(window, text="Recommencer", command=restart_game)
recommencer_button.pack(side=tk.RIGHT, padx=10, pady=10)

quitter_button = tk.Button(window, text="Quitter", command=window.destroy)
quitter_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Run interface graphique
window.mainloop()
