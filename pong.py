from tkinter import *
from random import *
from time import *

hauteur = 500
largeur = 900

# Creation des composants
fenetre = Tk()
fenetre.title('Pong - Thibault Feugère')
canevas = Canvas(fenetre, width=largeur, height=hauteur, bg='black')

# Empêche de redimenssionner la fenêtre
fenetre.resizable(False,False)

# Creation de la balle
balle = canevas.create_oval(440, 240, 460, 260, fill="white", width=0, state="disabled")

# Placement des composants
canevas.grid()

# Boucle infinie
fenetre.mainloop()