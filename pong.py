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
x0 = 440
y0 = 240
v_x = 0.4
v_y = 0.1
balle = canevas.create_oval(x0, y0, (x0 + 20), (y0 + 20), fill="white", width=0, state="disabled")

# Definition de la fonction de mouvement

def mouvement():
    global x0, y0, v_x, v_y
    x0 += v_x
    y0 += v_y

    canevas.coords(balle, x0, y0, (x0 + 20), (y0 + 20))

    if (x0 + 20) > largeur:
        v_x = -(v_x)
    elif x0 < 0:
        v_x = -(v_x)
    elif (y0 + 20) > hauteur:
        v_y = -(v_y)
    elif y0 < 0:
        v_y = -(v_y)

    canevas.after(2, mouvement)
    return

# Placement des composants
canevas.grid()
mouvement()

# Boucle infinie
fenetre.mainloop()