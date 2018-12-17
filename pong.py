from tkinter import *
from random import *
from time import *

hauteur = 500
largeur = 900

# Creation des composants
fenetre = Tk()
fenetre.title('Pong - Thibault Feugère')
fenetre.resizable(False,False)
canevas = Canvas(fenetre, width=largeur, height=hauteur, bg='black')

# Placement des composants
canevas.grid()

# Boucle infinie
fenetre.mainloop()