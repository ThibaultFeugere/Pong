from tkinter import *
from random import *
from time import *

# Dimensions
hauteur = 500
largeur = 900

# Scores
score1 = 0
score2 = 0
suppr_score_1 = 0
suppr_score_2 = 0

# Status du jeu
game_is_launch = False

# Creation des composants
fenetre = Tk()
fenetre.title('Pong - Thibault Feugere')
canevas = Canvas(fenetre, width=largeur, height=hauteur, bg='black')

# Delimitation
barre_verticale = canevas.create_line((largeur/2), 0, (largeur/2), hauteur, fill="red", dash=(2,2))

# Empeche de redimenssionner la fenetre
fenetre.resizable(False,False)