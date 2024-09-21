# Task 1.1

import pyjokes
# blague = pyjokes.get_joke(category='chuck')  # Obtenir une blague Chuck Norris
# print(blague)

# #Task 1.2

import turtle

# window = turtle.Screen()                  # Initialiser la fenêtre graphique
# ma_tortue = turtle.Turtle()               # Créer une tortue
#                                           # Boucle pour dessiner un carré (4 côtés)
# for _ in range(4):
#     ma_tortue.forward(100)                # Avancer de 100 unités
#     ma_tortue.right(90)                   # Tourner de 90 degrés vers la droite

# window.mainloop()                         # Fermer la fenêtre en cliquant

# Task 2.2

# #Can you explain precisely the following snippet of code? Which drawing will you see?
# window = turtle.Screen()
# toto = turtle.Screen ()
# toto . bgcolor("black")
# titi = turtle.Turtle ()
# titi.color("red")
# for i in range (3) :
#     titi.right(90)
#     titi . circle (42)
#     toto . exitonclick ()
# window.mainloop() 

# import turtle

#                                       # Création de la fenêtre turtle
# window = turtle.Screen()              # Un seul objet Screen
# window.bgcolor("black")               # Définir la couleur de fond de la fenêtre


# titi = turtle.Turtle()                 # Création de la tortue
# titi.color("red")                      # Définir la couleur de dessin de la tortue

#                                        # Dessin de trois cercles avec des rotations
# for i in range(3):
#     titi.right(90)                      # Tourner la tortue de 90 degrés
#     titi.circle(42)                      # Dessiner un cercle de rayon 42

#                                          # Garder la fenêtre ouverte jusqu'à un clic
# window.exitonclick()


# Task 2.3

# import turtle

# def draw_polygon(sides):
#     if sides < 3:
#         print("Un polygone doit avoir au moins 3 côtés.")
#         return

#     polygon_turtle = turtle.Turtle()                   # Créer une tortue

#     angle = 360 / sides                                # Calcul de l'angle extérieur pour chaque côté du polygone

#     length = 100                                       # Longueur des côtés (modifiable)

#                                                        # Dessiner le polygone
#     for _ in range(sides):
#         polygon_turtle.forward(length)                 # Avancer de 'length' unités
#         polygon_turtle.right(angle)                    # Tourner de 'angle' degrés

    
#     turtle.done()                                      # Garder la fenêtre ouverte jusqu'à un clic


# draw_polygon(6)  # Cela dessinera un pentagone
#sides = int(input("Entrez le nombre de côtés du polygone : "))
#draw_polygon(sides)
# Exemple d'utilisation : pour tester


# task 3 

# import turtle

# def draw_spiral():
   
#     spiral_turtle = turtle.Turtle()                  # Créer une tortue
    
#     spiral_turtle.speed(0)                           # Réglage de la vitesse (1 lente, 10 rapide, 0 la plus rapide)

#                                                      # Début de la spirale
#     length = 1                                       # Longueur initiale du segment
#     angle = 30                                       # Angle de rotation à chaque étape

#                                                      # Boucle pour créer la spirale
#     for _ in range(100):                             # Nombre d'itérations pour la spirale
#         spiral_turtle.forward(length)                # Avancer
#         spiral_turtle.right(angle)                   # Tourner d'un certain angle
#         length += 1                                  # Augmenter la longueur à chaque itération

#     turtle.done()                                    # Garder la fenêtre ouverte jusqu'à un clic

#Appeler la fonction pour dessiner la spirale
#draw_spiral()

#Task Challenge



# import turtle

# def sierpinski_triangle(points, depth):
#     if depth == 0:
#         t.penup()
#         t.goto(points[0])
#         t.pendown()
#         t.goto(points[1])
#         t.goto(points[2])
#         t.goto(points[0])
#     else:
#         mid1 = midpoint(points[0], points[1])
#         mid2 = midpoint(points[1], points[2])
#         mid3 = midpoint(points[0], points[2])
#         sierpinski_triangle([points[0], mid1, mid3], depth-1)
#         sierpinski_triangle([mid1, points[1], mid2], depth-1)
#         sierpinski_triangle([mid3, mid2, points[2]], depth-1)

# def midpoint(point1, point2):
#     return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

# def draw_sierpinski():
#     global t
#     t = turtle.Turtle()
#     t.speed(0)
#     points = [[-200, -100], [0, 200], [200, -100]]  # Points for the large triangle
#     sierpinski_triangle(points, 4)  # 4 is the depth of recursion

#     turtle.done()

# draw_sierpinski()



# Task 3.1

# import pygame
# import sys
# import turtle

# # Initialize pygame
# pygame.init()

# # Set up the display
# width, height = 600, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Hangman")

# # Load background image
# background_image = pygame.image.load('C:/Users/AMEVOR kossi/Downloads/2.png')

# # Resize image to fit the window
# background_image = pygame.transform.scale(background_image, (width, height))

# # Function to draw Sierpinski triangle using turtle graphics
# def sierpinski_triangle(points, depth):
#     if depth == 0:
#         t.penup()
#         t.goto(points[0])
#         t.pendown()
#         t.goto(points[1])
#         t.goto(points[2])
#         t.goto(points[0])
#     else:
#         mid1 = midpoint(points[0], points[1])
#         mid2 = midpoint(points[1], points[2])
#         mid3 = midpoint(points[0], points[2])
#         sierpinski_triangle([points[0], mid1, mid3], depth-1)
#         sierpinski_triangle([mid1, points[1], mid2], depth-1)
#         sierpinski_triangle([mid3, mid2, points[2]], depth-1)

# def midpoint(point1, point2):
#     return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

# def draw_sierpinski():
#     global t
#     t = turtle.Turtle()
#     t.speed(0)
#     points = [[-200, -100], [0, 200], [200, -100]]  # Points for the large triangle
#     sierpinski_triangle(points, 4)  # 4 is the depth of recursion
#     turtle.done()

# # Main loop to keep the window open
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Blit the background image
#     screen.blit(background_image, (0, 0))

#     # Update display
#     pygame.display.flip()

# pygame.quit()
# sys.exit()

# # Execute Turtle graphics code after Pygame window closes
# draw_sierpinski()

import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set up the display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")

# Load and resize background image
background_image = pygame.image.load('C:/Users/AMEVOR kossi/Downloads/1.png')
background_image = pygame.transform.scale(background_image, (width, height))

# Function to draw Sierpinski triangle using Pygame
def sierpinski_triangle(screen, points, depth, color):
    if depth == 0:
        pygame.draw.polygon(screen, color, points)
    else:
        mid1 = midpoint(points[0], points[1])
        mid2 = midpoint(points[1], points[2])
        mid3 = midpoint(points[0], points[2])
        sierpinski_triangle(screen, [points[0], mid1, mid3], depth-1, color)
        sierpinski_triangle(screen, [mid1, points[1], mid2], depth-1, color)
        sierpinski_triangle(screen, [mid3, mid2, points[2]], depth-1, color)

def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

# Function to draw a spiral using Pygame
def draw_spiral(screen, center, max_length, angle, color):
    length = 1
    spiral_surface = pygame.Surface((width, height), pygame.SRCALPHA)  # Create a transparent surface
    spiral_surface.fill((0, 0, 0, 0))  # Fill with transparent color
    x, y = center

    for _ in range(max_length):
        end_x = x + length * math.cos(math.radians(angle))
        end_y = y + length * math.sin(math.radians(angle))
        pygame.draw.line(spiral_surface, color, (x, y), (end_x, end_y), 1)
        x, y = end_x, end_y
        length += 1

    screen.blit(spiral_surface, (0, 0))  # Blit the spiral surface to the main screen

# Function to draw a stickman using Pygame
def draw_stickman(screen, position, scale=1, color=(0, 0, 0)):
    x, y = position
    head_radius = 20 * scale
    body_length = 50 * scale
    limb_length = 40 * scale

    # Head
    pygame.draw.circle(screen, color, (x, y), head_radius, 2)

    # Body
    pygame.draw.line(screen, color, (x, y + head_radius), (x, y + head_radius + body_length), 2)

    # Arms
    pygame.draw.line(screen, color, (x - limb_length, y + head_radius + 20), (x + limb_length, y + head_radius + 20), 2)

    # Legs
    pygame.draw.line(screen, color, (x, y + head_radius + body_length), (x - limb_length, y + head_radius + body_length + limb_length), 2)
    pygame.draw.line(screen, color, (x, y + head_radius + body_length), (x + limb_length, y + head_radius + body_length + limb_length), 2)

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    # Define points for the large triangle
    points = [(100, 500), (300, 100), (500, 500)]  # Adjust points to fit your window

    # Draw Sierpinski triangle in red
    sierpinski_triangle(screen, points, 4, (255, 0, 0))  # Depth 4, red color

    # Draw spiral in green
    draw_spiral(screen, (width // 2, height // 2), 100, 30, (0, 255, 0))  # Max length, angle, green color

    # Draw stickman in the center
    draw_stickman(screen, (width // 2, height // 2 + 100), scale=1, color=(0, 0, 0))  # Position, scale, color

    pygame.display.flip()

pygame.quit()
sys.exit()
 