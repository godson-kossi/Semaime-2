import tkinter as tk  # Importation de la bibliothèque tkinter pour l'interface graphique
from tkinter import simpledialog, messagebox  # Importation des dialogues simples et des boîtes de message
from PIL import Image, ImageTk  # Importation de PIL pour la gestion des images
import random  # Importation pour générer des valeurs aléatoires
import time  # Importation pour la gestion du temps

# Liste des mots à deviner
word_list = ["JAURES", "SAMUEL", "RUBY", "C", "LEO", "KOSSI", "GO", "BELINDA", "TOM", "ARTHUR", "ALEXANDRE", "VICTOR", "CONSTANT"]

# Niveaux d'étoiles avec caractères associés
star_level1_chars = {'A', 'E', 'I', 'O', 'U'}  # Lettres pour le niveau 1
star_level2_chars = {'T', 'R', 'N', 'S'}  # Lettres pour le niveau 2

# Variables globales
remaining_attempts = 5  # Nombre d'essais restants
score = 0  # Score du joueur
level = 1  # Niveau actuel du jeu
entry_boxes = []  # Liste pour stocker les cases de saisie
word_to_guess = ""  # Mot à deviner
masked_word = []  # Mot masqué avec des underscores
best_score = 0  # Meilleur score
target_score = 0  # Objectif de score
start_time = None  # Temps de début

# Classe pour afficher le temps dans un cercle
class TimeCircle(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  # Appel du constructeur de la classe parente
        # Création d'un cercle pour afficher le temps
        self.create_oval(0, 0, kwargs['width'], kwargs['height'], outline='black', width=2)
        # Création du texte au centre du cercle
        self.text_id = self.create_text(kwargs['width'] // 2, kwargs['height'] // 2, text="", font=('Arial', 10))

    # Méthode pour mettre à jour le texte du cercle
    def update_time(self, time_str):
        self.itemconfig(self.text_id, text=time_str)  # Met à jour le texte affiché

# Fonction pour dessiner le bonhomme pendu
def draw_hangman(attempts):
    canvas.delete("hangman")  # Supprime les éléments du bonhomme pendu précédents

    base_x = 250  # Position x de la base
    base_y = 80   # Position y de la base
    cord_length = 20  # Longueur des cordes

    # Dessine les différentes parties du bonhomme selon le nombre d'essais restants
    if attempts < 1:  # Tête
        canvas.create_oval(base_x - 20, base_y + cord_length - 20, base_x + 20, base_y + cord_length + 20, outline="black", width=2, tags="hangman")
    if attempts < 1:  # Corps
        canvas.create_line(base_x, base_y + cord_length, base_x, base_y + cord_length + 50, fill="black", width=2, tags="hangman")
    if attempts < 1:  # Bras gauche
        canvas.create_line(base_x, base_y + cord_length + 10, base_x - 30, base_y + cord_length + 40, fill="black", width=2, tags="hangman")
    if attempts < 1:  # Bras droit
        canvas.create_line(base_x, base_y + cord_length + 10, base_x + 30, base_y + cord_length + 40, fill="black", width=2, tags="hangman")
    if attempts < 1:  # Jambe gauche
        canvas.create_line(base_x, base_y + cord_length + 50, base_x - 30, base_y + cord_length + 100, fill="black", width=2, tags="hangman")
    if attempts < 1:  # Jambe droite
        canvas.create_line(base_x, base_y + cord_length + 50, base_x + 30, base_y + cord_length + 100, fill="black", width=2, tags="hangman")

# Fonction pour démarrer un nouveau niveau
def start_new_level(attempts_label, score_label, level_label):
    global remaining_attempts, word_to_guess, masked_word, entry_boxes, start_time

    word_to_guess = random.choice(word_list)  # Choisir un mot aléatoire
    masked_word = ["_" for _ in word_to_guess]  # Masquer le mot avec des underscores
    remaining_attempts = 5  # Réinitialiser les essais restants
    start_time = time.time()  # Enregistrer le temps de début

    for entry in entry_boxes:
        entry.destroy()  # Détruire les anciennes cases de saisie
    
    entry_boxes.clear()  # Vider la liste des cases de saisie

    for i, _ in enumerate(word_to_guess):
        # Créer une nouvelle case de saisie pour chaque lettre du mot
        entry = tk.Entry(window, width=2, font=('Arial', 18), justify='center')
        entry.place(x=180 + i * 40, y=300)  # Placer la case
        entry.insert(0, "_")  # Insérer un underscore
        entry.config(state="disabled")  # Désactiver la case
        entry_boxes.append(entry)  # Ajouter à la liste

    # Mettre à jour les étiquettes de statut
    attempts_label.config(text=f"Essais restants: {remaining_attempts}")
    score_label.config(text=f"Score: {score}")
    level_label.config(text=f"Niveau: {level}")

    draw_hangman(remaining_attempts)  # Dessiner le bonhomme en fonction des essais restants

# Fonction pour gérer le clic sur une lettre
def on_letter_click(letter, attempts_label, score_label, level_label, hour_circle, minute_circle, second_circle):
    global remaining_attempts, score, word_to_guess, level, best_score

    if letter in word_to_guess:  # Vérifie si la lettre est dans le mot
        for i, char in enumerate(word_to_guess):
            if char == letter:  # Si la lettre correspond
                masked_word[i] = letter  # Mettre à jour le mot masqué
                entry_boxes[i].config(state="normal")  # Activer la case
                entry_boxes[i].delete(0, tk.END)  # Effacer l'underscore
                entry_boxes[i].insert(0, letter)  # Insérer la lettre
                entry_boxes[i].config(state="disabled")  # Désactiver la case
                
        if "_" not in masked_word:  # Si le mot est complètement deviné
            # Mise à jour du score selon les lettres trouvées
            if any(char in star_level1_chars for char in word_to_guess):
                score += 2
            if any(char in star_level2_chars for char in word_to_guess):
                score += 3
            
            if len(word_to_guess) > 4:  # Bonus pour les mots longs
                score += 3
            else:
                score += 1
            
            score_label.config(text=f"Score: {score}")  # Mettre à jour l'étiquette de score
            
            level += 1  # Passer au niveau suivant
            if score > best_score:  # Vérifier si le score est un nouveau meilleur score
                best_score = score
            messagebox.showinfo("Gagné", f"Félicitations ! Vous passez au niveau {level}.")  # Alerte de victoire
            start_new_level(attempts_label, score_label, level_label)  # Démarrer un nouveau niveau
            return
    
    else:
        remaining_attempts -= 1  # Réduire le nombre d'essais restants
        attempts_label.config(text=f"Essais restants: {remaining_attempts}")  # Mettre à jour l'étiquette des essais
        draw_hangman(remaining_attempts)  # Dessiner le bonhomme en fonction des essais restants
        
        if remaining_attempts == 0:  # Si plus d'essais
            messagebox.showinfo("Perdu", f"Dommage ! Vous avez perdu. Le mot était {word_to_guess}.")  # Alerte de perte
            return

# Fonction pour demander l'objectif de score à l'utilisateur
def ask_for_target_score():
    global target_score
    target_score_str = simpledialog.askstring("Objectif du Score", "Entrez l'objectif de score:")  # Demander à l'utilisateur
    if target_score_str is not None:  # Si l'utilisateur a saisi une valeur
        try:
            target_score = int(target_score_str)  # Convertir en entier
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")  # Alerte d'erreur
            ask_for_target_score()  # Redemander l'objectif de score

# Fonction pour mettre à jour l'horloge
def update_clock(clock_label):
    current_time = time.strftime('%H:%M:%S')  # Obtenir l'heure actuelle
    clock_label.config(text=f"Temps act: {current_time}")  # Mettre à jour l'étiquette de l'horloge
    window.after(1000, update_clock, clock_label)  # Rappeler la fonction après 1 seconde

# Fonction pour mettre à jour le temps écoulé
def update_elapsed_time(hour_circle, minute_circle, second_circle):
    global start_time
    if start_time:  # Si le temps de début est défini
        elapsed_time = time.time() - start_time  # Calculer le temps écoulé
        hours, remainder = divmod(int(elapsed_time), 3600)  # Diviser en heures et reste
        minutes, seconds = divmod(remainder, 60)  # Diviser le reste en minutes et secondes
        hour_circle.update_time(f"{hours:02}")  # Mettre à jour l'horloge pour les heures
        minute_circle.update_time(f"{minutes:02}")  # Mettre à jour l'horloge pour les minutes
        second_circle.update_time(f"{seconds:02}")  # Mettre à jour l'horloge pour les secondes
    window.after(1000, update_elapsed_time, hour_circle, minute_circle, second_circle)  # Rappeler la fonction après 1 seconde

# Fonction principale pour l'interface du jeu du pendu
def hangman_gui():
    global entry_boxes, window, canvas
    
    window = tk.Tk()  # Créer la fenêtre principale
    window.title("Jeu du Pendu")  # Titre de la fenêtre
    window.geometry("600x400")  # Taille de la fenêtre

    ask_for_target_score()  # Demander l'objectif de score

    # Charger et redimensionner l'image d'arrière-plan
    background_img = Image.open('C:/Users/AMEVOR kossi/Downloads/2.png')  # Chemin de l'image
    background_img = background_img.resize((600, 400), Image.LANCZOS)  # Redimensionner l'image
    bg_photo = ImageTk.PhotoImage(background_img)  # Convertir l'image en format compatible avec Tkinter

    canvas = tk.Canvas(window, width=600, height=400)  # Créer un canevas
    canvas.pack(fill="both", expand=True)  # Remplir la fenêtre avec le canevas

    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)  # Ajouter l'image d'arrière-plan au canevas

    # Dessiner le cadre du jeu du pendu
    canvas.create_line(200, 50, 200, 220, width=9)  # Poteau vertical
    canvas.create_line(200, 50, 250, 50, width=5)   # Poteau horizontal
    canvas.create_line(250, 50, 250, 80, width=3)   # Corde

    # Étiquettes pour afficher les étoiles
    star_label1 = tk.Label(window, text="⭐", font=('Arial', 12), bg="#87CEEB")
    star_label1.place(x=10, y=300)
    
    star_label2 = tk.Label(window, text="⭐⭐", font=('Arial', 12), bg="#FFD700")
    star_label2.place(x=10, y=350)

    # Étiquette pour l'horloge
    clock_label = tk.Label(window, text="", font=('Arial', 12), bg="#87CEEB")
    clock_label.place(x=430, y=140)
    update_clock(clock_label)  # Mettre à jour l'horloge

    # Cercles pour afficher les heures, minutes et secondes
    hour_circle = TimeCircle(window, width=25, height=25)
    hour_circle.place(x=10, y=100)
    
    minute_circle = TimeCircle(window, width=25, height=25)
    minute_circle.place(x=40, y=100)
    
    second_circle = TimeCircle(window, width=25, height=25)
    second_circle.place(x=70, y=100)

    update_elapsed_time(hour_circle, minute_circle, second_circle)  # Mettre à jour le temps écoulé

    # Boutons pour chaque lettre de l'alphabet
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_buttons = {}
    for i, letter in enumerate(letters):
        btn = tk.Button(window, text=letter, width=3, height=1, font=('Arial', 12),
                        bg="#D2B48C", fg="white", 
                        command=lambda l=letter: on_letter_click(l, attempts_label, score_label, level_label, hour_circle, minute_circle, second_circle))
        btn.place(x=435 + (i % 4) * 40, y=185 + (i // 4) * 30)  # Placer les boutons
        letter_buttons[letter] = btn  # Ajouter le bouton au dictionnaire

    # Cadre pour afficher le score et le niveau
    score_frame = tk.Frame(window, bg="#87CEEB")
    score_frame.place(x=10, y=10, width=380, height=30)

    level_label = tk.Label(score_frame, text=f"Niveau: {level}", font=('Arial', 10), bg="#87CEEB")
    level_label.grid(row=0, column=0, padx=5)
    
    tk.Label(score_frame, text=f"Objectif: {target_score}", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=1, padx=5)
    tk.Label(score_frame, text=f"Meilleur: {best_score}", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=2, padx=5)
    
    score_label = tk.Label(score_frame, text=f"Score: {score}", font=('Arial', 10), bg="#87CEEB")
    score_label.grid(row=0, column=3, padx=5)

    # Étiquette pour les essais restants
    attempts_label = tk.Label(window, text=f"Essais restants: {remaining_attempts}", font=('Arial', 10), bg="#87CEEB")
    attempts_label.place(x=180, y=350)

    start_new_level(attempts_label, score_label, level_label)  # Démarrer le premier niveau

    window.mainloop()  # Lancer la boucle principale de l'interface graphique

hangman_gui()  # Appeler la fonction principale pour démarrer le jeu
