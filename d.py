# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk  # Pour la gestion des images

# # Le mot à deviner
# word_to_guess = "PYTHON"  # Exemple de mot à deviner
# masked_word = ["_" for _ in word_to_guess]  # Masque le mot avec des tirets

# # Nombre d'essais restants
# remaining_attempts = 5

# def on_letter_click(letter, word_label, attempts_label):
#     global remaining_attempts
    
#     # Si la lettre est dans le mot
#     if letter in word_to_guess:
#         for i, char in enumerate(word_to_guess):
#             if char == letter:
#                 masked_word[i] = letter  # Remplace le tiret par la lettre correcte
        
#         # Mise à jour de l'affichage du mot
#         word_label.config(text=" ".join(masked_word))
        
#         # Vérifie si le mot est complètement découvert
#         if "_" not in masked_word:
#             messagebox.showinfo("Gagné", "Félicitations ! Vous avez deviné le mot.")
#             return
    
#     else:
#         # Si la lettre est incorrecte, réduire les essais
#         remaining_attempts -= 1
#         attempts_label.config(text=f"Essais restants: {remaining_attempts}")
        
#         # Vérifie si le joueur a épuisé ses essais
#         if remaining_attempts == 0:
#             messagebox.showinfo("Perdu", f"Dommage ! Vous avez perdu. Le mot était {word_to_guess}.")
#             return

# def hangman_gui():
#     global remaining_attempts
    
#     # Créer la fenêtre principale
#     window = tk.Tk()
#     window.title("Jeu du Pendu")
#     window.geometry("600x400")  # Taille de la fenêtre réduite à 400x300

#     # Charger l'image de fond
#     background_img = Image.open('C:/Users/AMEVOR kossi/Downloads/2.png')
#     background_img = background_img.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionner à 400x300
#     bg_photo = ImageTk.PhotoImage(background_img)

#     # Créer le Canvas pour le fond et la zone du pendu
#     canvas = tk.Canvas(window, width=600, height=400)
#     canvas.pack(fill="both", expand=True)

#     # Afficher l'image de fond
#     canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

#     # Afficher le poteau du pendu (statique)
#     canvas.create_line(200, 50, 200, 150, width=5)  # Poteau vertical
#     canvas.create_line(200, 50, 250, 50, width=5)   # Poteau horizontal
#     canvas.create_line(250, 50, 250, 80, width=5)   # Corde

#     # Afficher le mot en cours (avec les tirets)
#     word_label = tk.Label(window, text=" ".join(masked_word), font=('Arial', 18), bg="#F9D342")
#     word_label.place(x=180, y=300)

#     # Créer les boutons pour chaque lettre
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letter_buttons = {}
#     for i, letter in enumerate(letters):
#         btn = tk.Button(window, text=letter, width=3, height=1, font=('Arial', 12),
#                         bg="#D2B48C", fg="white", 
#                         command=lambda l=letter: on_letter_click(l, word_label, attempts_label))
#         # Ajuster la position pour les placer sur le côté droit de l'écran
#         btn.place(x=435 + (i % 4) * 40, y=185 + (i // 4) * 30)  # Ajuster la position pour qu'elles apparaissent à droite
#         letter_buttons[letter] = btn

#     # Ajouter une section pour le score
#     score_frame = tk.Frame(window, bg="#87CEEB")
#     score_frame.place(x=10, y=10, width=380, height=30)

#     tk.Label(score_frame, text="Niveau: 4", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=0, padx=5)
#     tk.Label(score_frame, text="Objectif: 250", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=1, padx=5)
#     tk.Label(score_frame, text="Meilleur: 24", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=2, padx=5)
#     tk.Label(score_frame, text="Score: 0", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=3, padx=5)

#     # Ajout d'une étiquette pour le nombre d'essais restants
#     attempts_label = tk.Label(window, text=f"Essais restants: {remaining_attempts}", font=('Arial', 10), bg="#87CEEB")
#     attempts_label.place(x=180, y=300)

#     window.mainloop()

# hangman_gui()







# Task 2


# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk  # Pour la gestion des images
# import random
# # Le mot à deviner
# word_list = ["PYTHON", "JAVA", "JAVASCRIPT", "RUBY", "CPLUSPLUS", "HTML", "CSS", "TYPESCRIPT"]
# word_to_guess = random.choice(word_list)  # Sélectionne un mot aléatoire dans la liste
# masked_word = ["_" for _ in word_to_guess]  # Masque le mot avec des tirets

# # Nombre d'essais restants
# remaining_attempts = 5
# entry_boxes = []  # Liste des cases pour afficher les lettres du mot

# def on_letter_click(letter, attempts_label):
#     global remaining_attempts
    
#     # Si la lettre est dans le mot
#     if letter in word_to_guess:
#         for i, char in enumerate(word_to_guess):
#             if char == letter:
#                 masked_word[i] = letter  # Remplace le tiret par la lettre correcte
#                 entry_boxes[i].config(state="normal")  # Activer temporairement la case
#                 entry_boxes[i].delete(0, tk.END)  # Effacer la case
#                 entry_boxes[i].insert(0, letter)  # Afficher la lettre dans la case
#                 entry_boxes[i].config(state="disabled")  # Désactiver à nouveau la case
                
#         # Vérifie si le mot est complètement découvert
#         if "_" not in masked_word:
#             messagebox.showinfo("Gagné", "Félicitations ! Vous avez deviné le mot.")
#             return
    
#     else:
#         # Si la lettre est incorrecte, réduire les essais
#         remaining_attempts -= 1
#         attempts_label.config(text=f"Essais restants: {remaining_attempts}")
        
#         # Vérifie si le joueur a épuisé ses essais
#         if remaining_attempts == 0:
#             messagebox.showinfo("Perdu", f"Dommage ! Vous avez perdu. Le mot était {word_to_guess}.")
#             return

# def hangman_gui():
#     global remaining_attempts, entry_boxes
    
#     # Créer la fenêtre principale
#     window = tk.Tk()
#     window.title("Jeu du Pendu")
#     window.geometry("600x400")  # Taille de la fenêtre ajustée à 600x400

#     # Charger l'image de fond
#     background_img = Image.open('C:/Users/AMEVOR kossi/Downloads/2.png')
#     background_img = background_img.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionner à 600x400
#     bg_photo = ImageTk.PhotoImage(background_img)

#     # Créer le Canvas pour le fond et la zone du pendu
#     canvas = tk.Canvas(window, width=600, height=400)
#     canvas.pack(fill="both", expand=True)

#     # Afficher l'image de fond
#     canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

#     # Afficher le poteau du pendu (statique)
#     canvas.create_line(200, 50, 200, 150, width=5)  # Poteau vertical
#     canvas.create_line(200, 50, 250, 50, width=5)   # Poteau horizontal
#     canvas.create_line(250, 50, 250, 80, width=5)   # Corde

#     # Créer des cases pour le mot à deviner
#     for i, _ in enumerate(word_to_guess):
#         entry = tk.Entry(window, width=2, font=('Arial', 18), justify='center')
#         entry.place(x=80 + i * 40, y=300)  # Positionner chaque case
#         entry.insert(0, "_")  # Insérer un tiret pour chaque case vide
#         entry.config(state="disabled")  # Désactiver la saisie dans la case
#         entry_boxes.append(entry)  # Ajouter la case à la liste

#     # Créer les boutons pour chaque lettre
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letter_buttons = {}
#     for i, letter in enumerate(letters):
#         btn = tk.Button(window, text=letter, width=3, height=1, font=('Arial', 12),
#                         bg="#D2B48C", fg="white", 
#                         command=lambda l=letter: on_letter_click(l, attempts_label))
#         # Ajuster la position pour les placer sur le côté droit de l'écran
#         btn.place(x=435 + (i % 4) * 40, y=185 + (i // 4) * 30)  # Ajuster la position pour qu'elles apparaissent à droite
#         letter_buttons[letter] = btn

#     # Ajouter une section pour le score
#     score_frame = tk.Frame(window, bg="#87CEEB")
#     score_frame.place(x=10, y=10, width=380, height=30)

#     tk.Label(score_frame, text="Niveau: 4", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=0, padx=5)
#     tk.Label(score_frame, text="Objectif: 250", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=1, padx=5)
#     tk.Label(score_frame, text="Meilleur: 24", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=2, padx=5)
#     tk.Label(score_frame, text="Score: 0", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=3, padx=5)

#     # Ajout d'une étiquette pour le nombre d'essais restants
#     attempts_label = tk.Label(window, text=f"Essais restants: {remaining_attempts}", font=('Arial', 10), bg="#87CEEB")
#     attempts_label.place(x=180, y=350)

#     window.mainloop()

# hangman_gui()


# Task 3


# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk  # Pour la gestion des images
# import random  # Pour choisir un mot aléatoire

# # Liste des mots à deviner
# word_list = ["PYTHON", "JAVA", "RUBY", "C", "HTML", "CSS", "GO", "KOTLIN"]
# word_to_guess = random.choice(word_list)  # Sélectionne un mot aléatoire dans la liste
# masked_word = ["_" for _ in word_to_guess]  # Masque le mot avec des tirets

# # Nombre d'essais restants
# remaining_attempts = 5
# entry_boxes = []  # Liste des cases pour afficher les lettres du mot
# score = 0  # Initialiser le score à 0

# def on_letter_click(letter, attempts_label, score_label):
#     global remaining_attempts, score, word_to_guess
    
#     # Si la lettre est dans le mot
#     if letter in word_to_guess:
#         for i, char in enumerate(word_to_guess):
#             if char == letter:
#                 masked_word[i] = letter  # Remplace le tiret par la lettre correcte
#                 entry_boxes[i].config(state="normal")  # Activer temporairement la case
#                 entry_boxes[i].delete(0, tk.END)  # Effacer la case
#                 entry_boxes[i].insert(0, letter)  # Afficher la lettre dans la case
#                 entry_boxes[i].config(state="disabled")  # Désactiver à nouveau la case
                
#         # Vérifie si le mot est complètement découvert
#         if "_" not in masked_word:
#             if len(word_to_guess) > 4:
#                 score += 3  # Ajouter 3 points si le mot fait plus de 4 caractères
#             else:
#                 score += 1  # Ajouter 1 point si le mot fait 4 caractères ou moins
            
#             score_label.config(text=f"Score: {score}")  # Mettre à jour l'affichage du score
#             messagebox.showinfo("Gagné", f"Félicitations ! Vous avez deviné le mot : {word_to_guess}")
#             return
    
#     else:
#         # Si la lettre est incorrecte, réduire les essais
#         remaining_attempts -= 1
#         attempts_label.config(text=f"Essais restants: {remaining_attempts}")
        
#         # Vérifie si le joueur a épuisé ses essais
#         if remaining_attempts == 0:
#             messagebox.showinfo("Perdu", f"Dommage ! Vous avez perdu. Le mot était {word_to_guess}.")
#             return

# def hangman_gui():
#     global remaining_attempts, entry_boxes, word_to_guess, score
    
#     # Créer la fenêtre principale
#     window = tk.Tk()
#     window.title("Jeu du Pendu")
#     window.geometry("600x400")  # Taille de la fenêtre ajustée à 600x400

#     # Charger l'image de fond
#     background_img = Image.open('C:/Users/AMEVOR kossi/Downloads/2.png')
#     background_img = background_img.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionner à 600x400
#     bg_photo = ImageTk.PhotoImage(background_img)

#     # Créer le Canvas pour le fond et la zone du pendu
#     canvas = tk.Canvas(window, width=600, height=400)
#     canvas.pack(fill="both", expand=True)

#     # Afficher l'image de fond
#     canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

#     # Afficher le poteau du pendu (statique)
#     canvas.create_line(200, 50, 200, 150, width=5)  # Poteau vertical
#     canvas.create_line(200, 50, 250, 50, width=5)   # Poteau horizontal
#     canvas.create_line(250, 50, 250, 80, width=5)   # Corde

#     # Créer des cases pour le mot à deviner
#     entry_boxes = []  # Réinitialiser les cases à chaque lancement du jeu
#     for i, _ in enumerate(word_to_guess):
#         entry = tk.Entry(window, width=2, font=('Arial', 18), justify='center')
#         entry.place(x=180 + i * 40, y=300)  # Positionner chaque case
#         entry.insert(0, "_")  # Insérer un tiret pour chaque case vide
#         entry.config(state="disabled")  # Désactiver la saisie dans la case
#         entry_boxes.append(entry)  # Ajouter la case à la liste

#     # Créer les boutons pour chaque lettre
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letter_buttons = {}
#     for i, letter in enumerate(letters):
#         btn = tk.Button(window, text=letter, width=3, height=1, font=('Arial', 12),
#                         bg="#D2B48C", fg="white", 
#                         command=lambda l=letter: on_letter_click(l, attempts_label, score_label))
#         # Ajuster la position pour les placer sur le côté droit de l'écran
#         btn.place(x=435 + (i % 4) * 40, y=185 + (i // 4) * 30)  # Ajuster la position pour qu'elles apparaissent à droite
#         letter_buttons[letter] = btn

#     # Ajouter une section pour le score
#     score_frame = tk.Frame(window, bg="#87CEEB")
#     score_frame.place(x=10, y=10, width=380, height=30)

#     tk.Label(score_frame, text="Niveau: 4", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=0, padx=5)
#     tk.Label(score_frame, text="Objectif: 250", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=1, padx=5)
#     tk.Label(score_frame, text="Meilleur: 24", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=2, padx=5)
    
#     score_label = tk.Label(score_frame, text=f"Score: {score}", font=('Arial', 10), bg="#87CEEB")
#     score_label.grid(row=0, column=3, padx=5)

#     # Ajout d'une étiquette pour le nombre d'essais restants
#     attempts_label = tk.Label(window, text=f"Essais restants: {remaining_attempts}", font=('Arial', 10), bg="#87CEEB")
#     attempts_label.place(x=180, y=350)

#     window.mainloop()

# hangman_gui()



# Task 4

# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk  # Pour la gestion des images
# import random  # Pour choisir un mot aléatoire

# # Liste des mots à deviner
# word_list = ["PYTHON", "JAVA", "RUBY", "C", "HTML", "CSS", "GO", "KOTLIN"]

# # Nombre d'essais restants et score initial
# remaining_attempts = 5
# score = 0
# level = 1  # Niveau initial
# entry_boxes = []  # Liste des cases pour afficher les lettres du mot
# word_to_guess = ""  # Variable pour stocker le mot à deviner
# masked_word = []  # Variable pour masquer le mot

# def start_new_level(attempts_label, score_label, level_label):
#     global remaining_attempts, word_to_guess, masked_word, entry_boxes

#     # Choisir un nouveau mot aléatoire
#     word_to_guess = random.choice(word_list)
#     masked_word = ["_" for _ in word_to_guess]  # Masquer le mot avec des tirets
#     remaining_attempts = 5  # Réinitialiser le nombre d'essais

#     # Mise à jour des cases pour le nouveau mot
#     for entry in entry_boxes:
#         entry.destroy()  # Supprimer les anciennes cases
    
#     entry_boxes.clear()  # Vider la liste des anciennes cases

#     for i, _ in enumerate(word_to_guess):
#         entry = tk.Entry(window, width=2, font=('Arial', 18), justify='center')
#         entry.place(x=180 + i * 40, y=300)  # Positionner chaque case
#         entry.insert(0, "_")  # Insérer un tiret pour chaque case vide
#         entry.config(state="disabled")  # Désactiver la saisie dans la case
#         entry_boxes.append(entry)  # Ajouter la case à la liste

#     # Mise à jour des étiquettes (labels)
#     attempts_label.config(text=f"Essais restants: {remaining_attempts}")
#     score_label.config(text=f"Score: {score}")
#     level_label.config(text=f"Niveau: {level}")

# def on_letter_click(letter, attempts_label, score_label, level_label):
#     global remaining_attempts, score, word_to_guess, level
    
#     # Si la lettre est dans le mot
#     if letter in word_to_guess:
#         for i, char in enumerate(word_to_guess):
#             if char == letter:
#                 masked_word[i] = letter  # Remplacer le tiret par la lettre correcte
#                 entry_boxes[i].config(state="normal")  # Activer temporairement la case
#                 entry_boxes[i].delete(0, tk.END)  # Effacer la case
#                 entry_boxes[i].insert(0, letter)  # Afficher la lettre dans la case
#                 entry_boxes[i].config(state="disabled")  # Désactiver à nouveau la case
                
#         # Vérifie si le mot est complètement découvert
#         if "_" not in masked_word:
#             if len(word_to_guess) > 4:
#                 score += 3  # Ajouter 3 points si le mot fait plus de 4 caractères
#             else:
#                 score += 1  # Ajouter 1 point si le mot fait 4 caractères ou moins
            
#             # Mise à jour du score
#             score_label.config(text=f"Score: {score}")
            
#             # Passer au niveau suivant
#             level += 1  # Augmenter le niveau
#             messagebox.showinfo("Gagné", f"Félicitations ! Vous passez au niveau {level}.")
#             start_new_level(attempts_label, score_label, level_label)
#             return
    
#     else:
#         # Si la lettre est incorrecte, réduire les essais
#         remaining_attempts -= 1
#         attempts_label.config(text=f"Essais restants: {remaining_attempts}")
        
#         # Vérifie si le joueur a épuisé ses essais
#         if remaining_attempts == 0:
#             messagebox.showinfo("Perdu", f"Dommage ! Vous avez perdu. Le mot était {word_to_guess}.")
#             return

# def hangman_gui():
#     global entry_boxes, window, word_to_guess  # Assurer que word_to_guess est accessible
    
#     # Créer la fenêtre principale
#     window = tk.Tk()
#     window.title("Jeu du Pendu")
#     window.geometry("600x400")  # Taille de la fenêtre ajustée à 600x400

#     # Charger l'image de fond
#     background_img = Image.open('C:/Users/AMEVOR kossi/Downloads/2.png')
#     background_img = background_img.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionner à 600x400
#     bg_photo = ImageTk.PhotoImage(background_img)

#     # Créer le Canvas pour le fond et la zone du pendu
#     canvas = tk.Canvas(window, width=600, height=400)
#     canvas.pack(fill="both", expand=True)

#     # Afficher l'image de fond
#     canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

#     # Afficher le poteau du pendu (statique)
#     canvas.create_line(200, 50, 200, 150, width=5)  # Poteau vertical
#     canvas.create_line(200, 50, 250, 50, width=5)   # Poteau horizontal
#     canvas.create_line(250, 50, 250, 80, width=5)   # Corde

#     # Créer les boutons pour chaque lettre
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letter_buttons = {}
#     for i, letter in enumerate(letters):
#         btn = tk.Button(window, text=letter, width=3, height=1, font=('Arial', 12),
#                         bg="#D2B48C", fg="white", 
#                         command=lambda l=letter: on_letter_click(l, attempts_label, score_label, level_label))
#         # Ajuster la position pour les placer sur le côté droit de l'écran
#         btn.place(x=435 + (i % 4) * 40, y=185 + (i // 4) * 30)  # Ajuster la position pour qu'elles apparaissent à droite
#         letter_buttons[letter] = btn

#     # Ajouter une section pour le score et le niveau
#     score_frame = tk.Frame(window, bg="#87CEEB")
#     score_frame.place(x=10, y=10, width=380, height=30)

#     level_label = tk.Label(score_frame, text=f"Niveau: {level}", font=('Arial', 10), bg="#87CEEB")
#     level_label.grid(row=0, column=0, padx=5)
    
#     tk.Label(score_frame, text="Objectif: 250", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=1, padx=5)
#     tk.Label(score_frame, text="Meilleur: 24", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=2, padx=5)
    
#     score_label = tk.Label(score_frame, text=f"Score: {score}", font=('Arial', 10), bg="#87CEEB")
#     score_label.grid(row=0, column=3, padx=5)

#     # Ajout d'une étiquette pour le nombre d'essais restants
#     attempts_label = tk.Label(window, text=f"Essais restants: {remaining_attempts}", font=('Arial', 10), bg="#87CEEB")
#     attempts_label.place(x=180, y=350)

#     # Démarrer le premier niveau
#     start_new_level(attempts_label, score_label, level_label)

#     window.mainloop()

# # Démarrer l'interface graphique
# hangman_gui()



# Task 5


# import tkinter as tk
# from tkinter import simpledialog, messagebox
# from PIL import Image, ImageTk  # Pour la gestion des images
# import random  # Pour choisir un mot aléatoire

# # Liste des mots à deviner
# word_list = ["PYTHON", "JAVA", "RUBY", "C", "HTML", "CSS", "GO", "KOTLIN"]

# # Variables globales
# remaining_attempts = 5
# score = 0
# level = 1  # Niveau initial
# entry_boxes = []  # Liste des cases pour afficher les lettres du mot
# word_to_guess = ""  # Variable pour stocker le mot à deviner
# masked_word = []  # Variable pour masquer le mot
# best_score = 0  # Meilleur score du joueur
# target_score = 0  # Objectif du score

# def start_new_level(attempts_label, score_label, level_label):
#     global remaining_attempts, word_to_guess, masked_word, entry_boxes

#     # Choisir un nouveau mot aléatoire
#     word_to_guess = random.choice(word_list)
#     masked_word = ["_" for _ in word_to_guess]  # Masquer le mot avec des tirets
#     remaining_attempts = 5  # Réinitialiser le nombre d'essais

#     # Mise à jour des cases pour le nouveau mot
#     for entry in entry_boxes:
#         entry.destroy()  # Supprimer les anciennes cases
    
#     entry_boxes.clear()  # Vider la liste des anciennes cases

#     for i, _ in enumerate(word_to_guess):
#         entry = tk.Entry(window, width=2, font=('Arial', 18), justify='center')
#         entry.place(x=180 + i * 40, y=300)  # Positionner chaque case
#         entry.insert(0, "_")  # Insérer un tiret pour chaque case vide
#         entry.config(state="disabled")  # Désactiver la saisie dans la case
#         entry_boxes.append(entry)  # Ajouter la case à la liste

#     # Mise à jour des étiquettes (labels)
#     attempts_label.config(text=f"Essais restants: {remaining_attempts}")
#     score_label.config(text=f"Score: {score}")
#     level_label.config(text=f"Niveau: {level}")

# def on_letter_click(letter, attempts_label, score_label, level_label):
#     global remaining_attempts, score, word_to_guess, level, best_score
    
#     # Si la lettre est dans le mot
#     if letter in word_to_guess:
#         for i, char in enumerate(word_to_guess):
#             if char == letter:
#                 masked_word[i] = letter  # Remplacer le tiret par la lettre correcte
#                 entry_boxes[i].config(state="normal")  # Activer temporairement la case
#                 entry_boxes[i].delete(0, tk.END)  # Effacer la case
#                 entry_boxes[i].insert(0, letter)  # Afficher la lettre dans la case
#                 entry_boxes[i].config(state="disabled")  # Désactiver à nouveau la case
                
#         # Vérifie si le mot est complètement découvert
#         if "_" not in masked_word:
#             if len(word_to_guess) > 4:
#                 score += 3  # Ajouter 3 points si le mot fait plus de 4 caractères
#             else:
#                 score += 1  # Ajouter 1 point si le mot fait 4 caractères ou moins
            
#             # Mise à jour du score
#             score_label.config(text=f"Score: {score}")
            
#             # Passer au niveau suivant
#             level += 1  # Augmenter le niveau
#             if score > best_score:
#                 best_score = score  # Mettre à jour le meilleur score si nécessaire
#             messagebox.showinfo("Gagné", f"Félicitations ! Vous passez au niveau {level}.")
#             start_new_level(attempts_label, score_label, level_label)
#             return
    
#     else:
#         # Si la lettre est incorrecte, réduire les essais
#         remaining_attempts -= 1
#         attempts_label.config(text=f"Essais restants: {remaining_attempts}")
        
#         # Vérifie si le joueur a épuisé ses essais
#         if remaining_attempts == 0:
#             messagebox.showinfo("Perdu", f"Dommage ! Vous avez perdu. Le mot était {word_to_guess}.")
#             return

# def ask_for_target_score():
#     global target_score
#     target_score_str = simpledialog.askstring("Objectif du Score", "Entrez l'objectif de score:")
#     if target_score_str is not None:
#         try:
#             target_score = int(target_score_str)
#         except ValueError:
#             messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
#             ask_for_target_score()

# def hangman_gui():
#     global entry_boxes, window, word_to_guess  # Assurer que word_to_guess est accessible
    
#     # Créer la fenêtre principale
#     window = tk.Tk()
#     window.title("Jeu du Pendu")
#     window.geometry("600x400")  # Taille de la fenêtre ajustée à 600x400

#     # Demander à l'utilisateur l'objectif de score
#     ask_for_target_score()

#     # Charger l'image de fond
#     background_img = Image.open('C:/Users/AMEVOR kossi/Downloads/2.png')
#     background_img = background_img.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionner à 600x400
#     bg_photo = ImageTk.PhotoImage(background_img)

#     # Créer le Canvas pour le fond et la zone du pendu
#     canvas = tk.Canvas(window, width=600, height=400)
#     canvas.pack(fill="both", expand=True)

#     # Afficher l'image de fond
#     canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

#     # Afficher le poteau du pendu (statique)
#     canvas.create_line(200, 50, 200, 150, width=5)  # Poteau vertical
#     canvas.create_line(200, 50, 250, 50, width=5)   # Poteau horizontal
#     canvas.create_line(250, 50, 250, 80, width=5)   # Corde

#     # Créer les boutons pour chaque lettre
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letter_buttons = {}
#     for i, letter in enumerate(letters):
#         btn = tk.Button(window, text=letter, width=3, height=1, font=('Arial', 12),
#                         bg="#D2B48C", fg="white", 
#                         command=lambda l=letter: on_letter_click(l, attempts_label, score_label, level_label))
#         # Ajuster la position pour les placer sur le côté droit de l'écran
#         btn.place(x=435 + (i % 4) * 40, y=185 + (i // 4) * 30)  # Ajuster la position pour qu'elles apparaissent à droite
#         letter_buttons[letter] = btn

#     # Ajouter une section pour le score et le niveau
#     score_frame = tk.Frame(window, bg="#87CEEB")
#     score_frame.place(x=10, y=10, width=380, height=30)

#     level_label = tk.Label(score_frame, text=f"Niveau: {level}", font=('Arial', 10), bg="#87CEEB")
#     level_label.grid(row=0, column=0, padx=5)
    
#     tk.Label(score_frame, text=f"Objectif: {target_score}", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=1, padx=5)
#     tk.Label(score_frame, text=f"Meilleur: {best_score}", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=2, padx=5)
    
#     score_label = tk.Label(score_frame, text=f"Score: {score}", font=('Arial', 10), bg="#87CEEB")
#     score_label.grid(row=0, column=3, padx=5)

#     # Ajout d'une étiquette pour le nombre d'essais restants
#     attempts_label = tk.Label(window, text=f"Essais restants: {remaining_attempts}", font=('Arial', 10), bg="#87CEEB")
#     attempts_label.place(x=180, y=350)

#     # Démarrer le premier niveau
#     start_new_level(attempts_label, score_label, level_label)

#     window.mainloop()

# # Démarrer l'interface graphique
# hangman_gui()



# # Task 6


import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk  # Pour la gestion des images
import random  # Pour choisir un mot aléatoire

# Liste des mots à deviner
word_list = ["PYTHON", "JAVA", "RUBY", "C", "HTML", "CSS", "GO", "KOTLIN"]

# Niveaux d'étoiles avec caractères associés
star_level1_chars = {'A', 'E', 'I', 'O', 'U'}  # Liste de caractères pour le premier niveau d'étoiles
star_level2_chars = {'T', 'R', 'N', 'S'}  # Liste de caractères pour le deuxième niveau d'étoiles


# Variables globales
remaining_attempts = 5
score = 0
level = 1  # Niveau initial
entry_boxes = []  # Liste des cases pour afficher les lettres du mot
word_to_guess = ""  # Variable pour stocker le mot à deviner
masked_word = []  # Variable pour masquer le mot
best_score = 0  # Meilleur score du joueur
target_score = 0  # Objectif du score


# Variables globales
remaining_attempts = 5
score = 0
level = 1
entry_boxes = []
word_to_guess = ""
masked_word = []
best_score = 0
target_score = 0

def draw_hangman(attempts):
    canvas.delete("hangman")

    base_x = 250
    base_y = 80
    cord_length = 50

    if attempts < 6:  # Tête
        canvas.create_oval(base_x - 20, base_y + cord_length - 20, base_x + 20, base_y + cord_length + 20, outline="black", width=2, tags="hangman")
    if attempts < 5:  # Corps
        canvas.create_line(base_x, base_y + cord_length, base_x, base_y + cord_length + 50, fill="black", width=2, tags="hangman")
    if attempts < 4:  # Bras gauche
        canvas.create_line(base_x, base_y + cord_length + 10, base_x - 30, base_y + cord_length + 40, fill="black", width=2, tags="hangman")
    if attempts < 3:  # Bras droit
        canvas.create_line(base_x, base_y + cord_length + 10, base_x + 30, base_y + cord_length + 40, fill="black", width=2, tags="hangman")
    if attempts < 2:  # Jambe gauche
        canvas.create_line(base_x, base_y + cord_length + 50, base_x - 30, base_y + cord_length + 100, fill="black", width=2, tags="hangman")
    if attempts < 1:  # Jambe droite
        canvas.create_line(base_x, base_y + cord_length + 50, base_x + 30, base_y + cord_length + 100, fill="black", width=2, tags="hangman")

def start_new_level(attempts_label, score_label, level_label):
    global remaining_attempts, word_to_guess, masked_word, entry_boxes

    # Choisir un nouveau mot aléatoire
    word_to_guess = random.choice(word_list)
    masked_word = ["_" for _ in word_to_guess]  # Masquer le mot avec des tirets
    remaining_attempts = 5  # Réinitialiser le nombre d'essais

    # Mise à jour des cases pour le nouveau mot
    for entry in entry_boxes:
        entry.destroy()  # Supprimer les anciennes cases
    
    entry_boxes.clear()  # Vider la liste des anciennes cases

    for i, _ in enumerate(word_to_guess):
        entry = tk.Entry(window, width=2, font=('Arial', 18), justify='center')
        entry.place(x=180 + i * 40, y=300)  # Positionner chaque case
        entry.insert(0, "_")  # Insérer un tiret pour chaque case vide
        entry.config(state="disabled")  # Désactiver la saisie dans la case
        entry_boxes.append(entry)  # Ajouter la case à la liste

    # Mise à jour des étiquettes (labels)
    attempts_label.config(text=f"Essais restants: {remaining_attempts}")
    score_label.config(text=f"Score: {score}")
    level_label.config(text=f"Niveau: {level}")

#Réinitialiser le dessin du pendu
draw_hangman(remaining_attempts)


def on_letter_click(letter, attempts_label, score_label, level_label):
    global remaining_attempts, score, word_to_guess, level, best_score

    # Si la lettre est dans le mot
    if letter in word_to_guess:
        for i, char in enumerate(word_to_guess):
            if char == letter:
                masked_word[i] = letter  # Remplacer le tiret par la lettre correcte
                entry_boxes[i].config(state="normal")  # Activer temporairement la case
                entry_boxes[i].delete(0, tk.END)  # Effacer la case
                entry_boxes[i].insert(0, letter)  # Afficher la lettre dans la case
                entry_boxes[i].config(state="disabled")  # Désactiver à nouveau la case
                
        # Vérifie si le mot est complètement découvert
        if "_" not in masked_word:
            # Points supplémentaires basés sur les niveaux d'étoiles
            if any(char in star_level1_chars for char in word_to_guess):
                score += 2  # Ajouter 2 points pour le premier niveau d'étoiles
            if any(char in star_level2_chars for char in word_to_guess):
                score += 3  # Ajouter 3 points pour le deuxième niveau d'étoiles
            
            if len(word_to_guess) > 4:
                score += 3  # Ajouter 3 points si le mot fait plus de 4 caractères
            else:
                score += 1  # Ajouter 1 point si le mot fait 4 caractères ou moins
            
            # Mise à jour du score
            score_label.config(text=f"Score: {score}")
            
            # Passer au niveau suivant
            level += 1  # Augmenter le niveau
            if score > best_score:
                best_score = score  # Mettre à jour le meilleur score si nécessaire
            messagebox.showinfo("Gagné", f"Félicitations ! Vous passez au niveau {level}.")
            start_new_level(attempts_label, score_label, level_label)
            return
    
    else:
        # Si la lettre est incorrecte, réduire les essais
        remaining_attempts -= 1
        attempts_label.config(text=f"Essais restants: {remaining_attempts}")
        
        # Vérifie si le joueur a épuisé ses essais
        if remaining_attempts == 0:
            messagebox.showinfo("Perdu", f"Dommage ! Vous avez perdu. Le mot était {word_to_guess}.")
            return

def ask_for_target_score():
    global target_score
    target_score_str = simpledialog.askstring("Objectif du Score", "Entrez l'objectif de score:")
    if target_score_str is not None:
        try:
            target_score = int(target_score_str)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
            ask_for_target_score()

def hangman_gui():
    global entry_boxes, window, word_to_guess  # Assurer que word_to_guess est accessible
    
    # Créer la fenêtre principale
    window = tk.Tk()
    window.title("Jeu du Pendu")
    window.geometry("600x400")  # Taille de la fenêtre ajustée à 600x400

    # Demander à l'utilisateur l'objectif de score
    ask_for_target_score()

    # Charger l'image de fond
    background_img = Image.open('C:/Users/AMEVOR kossi/Downloads/2.png')
    background_img = background_img.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionner à 600x400
    bg_photo = ImageTk.PhotoImage(background_img)

    # Créer le Canvas pour le fond et la zone du pendu
    canvas = tk.Canvas(window, width=600, height=400)
    canvas.pack(fill="both", expand=True)

    # Afficher l'image de fond
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

    # Afficher le poteau du pendu (statique)
    canvas.create_line(200, 50, 200, 150, width=5)  # Poteau vertical
    canvas.create_line(200, 50, 250, 50, width=5)   # Poteau horizontal
    canvas.create_line(250, 50, 250, 80, width=5)   # Corde

    # Ajouter les niveaux d'étoiles à gauche
    star_label1 = tk.Label(window, text="⭐ ", font=('Arial', 12), bg="#87CEEB")
    star_label1.place(x=10, y=300)
    
    star_label2 = tk.Label(window, text=" ⭐⭐", font=('Arial', 12), bg="#FFD700")
    star_label2.place(x=10, y=350)

    # Créer les boutons pour chaque lettre
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_buttons = {}
    for i, letter in enumerate(letters):
        btn = tk.Button(window, text=letter, width=3, height=1, font=('Arial', 12),
                        bg="#D2B48C", fg="white", 
                        command=lambda l=letter: on_letter_click(l, attempts_label, score_label, level_label))
        # Ajuster la position pour les placer sur le côté droit de l'écran
        btn.place(x=435 + (i % 4) * 40, y=185 + (i // 4) * 30)  # Ajuster la position pour qu'elles apparaissent à droite
        letter_buttons[letter] = btn

    # Ajouter une section pour le score et le niveau
    score_frame = tk.Frame(window, bg="#87CEEB")
    score_frame.place(x=10, y=10, width=380, height=30)

    level_label = tk.Label(score_frame, text=f"Niveau: {level}", font=('Arial', 10), bg="#87CEEB")
    level_label.grid(row=0, column=0, padx=5)
    
    tk.Label(score_frame, text=f"Objectif: {target_score}", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=1, padx=5)
    tk.Label(score_frame, text=f"Meilleur: {best_score}", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=2, padx=5)
    
    score_label = tk.Label(score_frame, text=f"Score: {score}", font=('Arial', 10), bg="#87CEEB")
    score_label.grid(row=0, column=3, padx=5)

    # Ajout d'une étiquette pour le nombre d'essais restants
    attempts_label = tk.Label(window, text=f"Essais restants: {remaining_attempts}", font=('Arial', 10), bg="#87CEEB")
    attempts_label.place(x=180, y=350)

    # Démarrer le premier niveau
    start_new_level(attempts_label, score_label, level_label)

    window.mainloop()

# Démarrer l'interface graphique
hangman_gui()















# Task 9


# import tkinter as tk
# from tkinter import simpledialog, messagebox
# from PIL import Image, ImageTk  # Pour la gestion des images
# import random  # Pour choisir un mot aléatoire

# # Liste des mots à deviner
# word_list = ["PYTHON", "JAVA", "RUBY", "C", "HTML", "CSS", "GO", "KOTLIN"]

# # Niveaux d'étoiles avec caractères associés
# star_level1_chars = {'A', 'E', 'I', 'O', 'U'}  # Liste de caractères pour le premier niveau d'étoiles
# star_level2_chars = {'T', 'R', 'N', 'S'}  # Liste de caractères pour le deuxième niveau d'étoiles

# # Variables globales
# remaining_attempts = 5
# score = 0
# level = 1  # Niveau initial
# entry_boxes = []  # Liste des cases pour afficher les lettres du mot
# word_to_guess = ""  # Variable pour stocker le mot à deviner
# masked_word = []  # Variable pour masquer le mot
# best_score = 0  # Meilleur score du joueur
# target_score = 0  # Objectif du score

# # Fonction pour dessiner le joueur et le pendu
# def draw_hangman(attempts):
#     canvas.delete("hangman")  # Supprimer les anciens dessins
    
#     if attempts < 1:  # Tête
#         canvas.create_oval(180, 80, 220, 120, outline="black", width=1, tags="hangman")
#     if attempts < 1:  # Corps
#         canvas.create_line(200, 120, 200, 180, fill="black", width=1, tags="hangman")
#     if attempts < 1:  # Bras gauche
#         canvas.create_line(200, 130, 170, 150, fill="black", width=1, tags="hangman")
#     if attempts < 1:  # Bras droit
#         canvas.create_line(200, 130, 230, 150, fill="black", width=1, tags="hangman")
#     if attempts < 1:  # Jambe gauche
#         canvas.create_line(200, 180, 170, 230, fill="black", width=1, tags="hangman")
#     if attempts < 1:  # Jambe droite
#         canvas.create_line(200, 180, 230, 230, fill="black", width=1, tags="hangman")

# def start_new_level(attempts_label, score_label, level_label):
#     global remaining_attempts, word_to_guess, masked_word, entry_boxes

#     # Choisir un nouveau mot aléatoire
#     word_to_guess = random.choice(word_list)
#     masked_word = ["_" for _ in word_to_guess]  # Masquer le mot avec des tirets
#     remaining_attempts = 5  # Réinitialiser le nombre d'essais

#     # Mise à jour des cases pour le nouveau mot
#     for entry in entry_boxes:
#         entry.destroy()  # Supprimer les anciennes cases
    
#     entry_boxes.clear()  # Vider la liste des anciennes cases

#     for i, _ in enumerate(word_to_guess):
#         entry = tk.Entry(window, width=2, font=('Arial', 18), justify='center')
#         entry.place(x=180 + i * 40, y=300)  # Positionner chaque case
#         entry.insert(0, "_")  # Insérer un tiret pour chaque case vide
#         entry.config(state="disabled")  # Désactiver la saisie dans la case
#         entry_boxes.append(entry)  # Ajouter la case à la liste

#     # Mise à jour des étiquettes (labels)
#     attempts_label.config(text=f"Essais restants: {remaining_attempts}")
#     score_label.config(text=f"Score: {score}")
#     level_label.config(text=f"Niveau: {level}")

#     # Réinitialiser le dessin du pendu
#     draw_hangman(remaining_attempts)

# def on_letter_click(letter, attempts_label, score_label, level_label):
#     global remaining_attempts, score, word_to_guess, level, best_score

#     # Si la lettre est dans le mot
#     if letter in word_to_guess:
#         for i, char in enumerate(word_to_guess):
#             if char == letter:
#                 masked_word[i] = letter  # Remplacer le tiret par la lettre correcte
#                 entry_boxes[i].config(state="normal")  # Activer temporairement la case
#                 entry_boxes[i].delete(0, tk.END)  # Effacer la case
#                 entry_boxes[i].insert(0, letter)  # Afficher la lettre dans la case
#                 entry_boxes[i].config(state="disabled")  # Désactiver à nouveau la case
                
#         # Vérifie si le mot est complètement découvert
#         if "_" not in masked_word:
#             # Points supplémentaires basés sur les niveaux d'étoiles
#             if any(char in star_level1_chars for char in word_to_guess):
#                 score += 2  # Ajouter 2 points pour le premier niveau d'étoiles
#             if any(char in star_level2_chars for char in word_to_guess):
#                 score += 3  # Ajouter 3 points pour le deuxième niveau d'étoiles
            
#             if len(word_to_guess) > 4:
#                 score += 3  # Ajouter 3 points si le mot fait plus de 4 caractères
#             else:
#                 score += 1  # Ajouter 1 point si le mot fait 4 caractères ou moins
            
#             # Mise à jour du score
#             score_label.config(text=f"Score: {score}")
            
#             # Passer au niveau suivant
#             level += 1  # Augmenter le niveau
#             if score > best_score:
#                 best_score = score  # Mettre à jour le meilleur score si nécessaire
#             messagebox.showinfo("Gagné", f"Félicitations ! Vous passez au niveau {level}.")
#             start_new_level(attempts_label, score_label, level_label)
#             return
    
#     else:
#         # Si la lettre est incorrecte, réduire les essais
#         remaining_attempts -= 1
#         attempts_label.config(text=f"Essais restants: {remaining_attempts}")
#         draw_hangman(remaining_attempts)  # Mettre à jour le dessin du pendu
        
#         # Vérifie si le joueur a épuisé ses essais
#         if remaining_attempts == 0:
#             messagebox.showinfo("Perdu", f"Dommage ! Vous avez perdu. Le mot était {word_to_guess}.")
#             return

# def ask_for_target_score():
#     global target_score
#     target_score_str = simpledialog.askstring("Objectif du Score", "Entrez l'objectif de score:")
#     if target_score_str is not None:
#         try:
#             target_score = int(target_score_str)
#         except ValueError:
#             messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
#             ask_for_target_score()

# def hangman_gui():
#     global entry_boxes, window, word_to_guess, canvas  # Assurer que word_to_guess est accessible
    
#     # Créer la fenêtre principale
#     window = tk.Tk()
#     window.title("Jeu du Pendu")
#     window.geometry("600x400")  # Taille de la fenêtre ajustée à 600x400

#     # Demander à l'utilisateur l'objectif de score
#     ask_for_target_score()

#     # Charger l'image de fond
#     background_img = Image.open('C:/Users/AMEVOR kossi/Downloads/2.png')
#     background_img = background_img.resize((600, 400), Image.Resampling.LANCZOS)  # Redimensionner à 600x400
#     bg_photo = ImageTk.PhotoImage(background_img)

#     # Créer le Canvas pour le fond et la zone du pendu
#     canvas = tk.Canvas(window, width=600, height=400)
#     canvas.pack(fill="both", expand=True)

#     # Afficher l'image de fond
#     canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

#     # Afficher le poteau du pendu (statique)
#     canvas.create_line(200, 50, 200, 150, width=5)  # Poteau vertical
#     canvas.create_line(200, 50, 250, 50, width=5)   # Poteau horizontal
#     canvas.create_line(250, 50, 250, 80, width=5)   # Corde

#     # Ajouter les niveaux d'étoiles à gauche
#     star_label1 = tk.Label(window, text="⭐ Niveaux d'Étoiles 1", font=('Arial', 12), bg="#87CEEB")
#     star_label1.place(x=10, y=50)
    
#     star_label2 = tk.Label(window, text="⭐ Niveaux d'Étoiles 2", font=('Arial', 12), bg="#87CEEB")
#     star_label2.place(x=10, y=100)

#     # Afficher le mot en cours (avec les tirets)
#     word_label = tk.Label(window, text=" ".join(masked_word), font=('Arial', 18), bg="#F9D342")
#     word_label.place(x=180, y=300)

#     # Créer les boutons pour chaque lettre
#     letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     letter_buttons = {}
#     for i, letter in enumerate(letters):
#         btn = tk.Button(window, text=letter, width=3, height=1, font=('Arial', 12),
#                         bg="#D2B48C", fg="white",
#                         command=lambda l=letter: on_letter_click(l, attempts_label, score_label, level_label))
#         btn.place(x=435 + (i % 4) * 40, y=185 + (i // 4) * 30)
#         letter_buttons[letter] = btn

#     # Ajouter une section pour le score
#     score_frame = tk.Frame(window, bg="#87CEEB")
#     score_frame.place(x=10, y=10, width=380, height=30)

#     level_label = tk.Label(score_frame, text=f"Niveau: {level}", font=('Arial', 10), bg="#87CEEB")
#     level_label.grid(row=0, column=0, padx=5)

#     tk.Label(score_frame, text=f"Objectif: {target_score}", font=('Arial', 10), bg="#87CEEB").grid(row=0, column=1, padx=5)
    
#     score_label = tk.Label(score_frame, text=f"Score: {score}", font=('Arial', 10), bg="#87CEEB")
#     score_label.grid(row=0, column=2, padx=5)

#     # Ajout d'une étiquette pour le nombre d'essais restants
#     attempts_label = tk.Label(window, text=f"Essais restants: {remaining_attempts}", font=('Arial', 10), bg="#87CEEB")
#     attempts_label.place(x=180, y=350)

#     # Démarrer le premier niveau
#     start_new_level(attempts_label, score_label, level_label)

#     window.mainloop()

# # Démarrer l'interface graphique
# hangman_gui()
