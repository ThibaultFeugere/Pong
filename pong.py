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
balle_x0 = 440
balle_y0 = 240
balle_v_x = 0.4
balle_v_y = 0.1
balle = canevas.create_oval(balle_x0, balle_y0, (balle_x0 + 20), (balle_y0 + 20), fill="white", width=0, state="disabled")

# Creation raquette du joueur un
raq1_x0 = 5
raq1_y0 = 215
raq1_v_x = 5
raquette1 = canevas.create_rectangle(raq1_x0, raq1_y0, (raq1_x0 + 14), (raq1_y0 + 70), fill="white", width=0, state="disabled")

# Creation raquette du joueur deux
raq2_x0 = largeur - 4
raq2_y0 = 215
raq2_v_x = 5
raquette1 = canevas.create_rectangle(raq2_x0, raq2_y0, (raq2_x0 - 14), (raq2_y0 + 70), fill="white", width=0, state="disabled")

# Definition de la fonction de mouvement

def mouvement():
    global balle_x0, balle_y0, balle_v_x, balle_v_y
    balle_x0 += balle_v_x
    balle_y0 += balle_v_y

    canevas.coords(balle, balle_x0, balle_y0, (balle_x0 + 20), (balle_y0 + 20))

    if (balle_x0 + 20) > largeur:
        balle_v_x = -(balle_v_x)
    elif balle_x0 < 0:
        balle_v_x = -(balle_v_x)
    elif (balle_y0 + 20) > hauteur:
        balle_v_y = -(balle_v_y)
    elif balle_y0 < 0:
        balle_v_y = -(balle_v_y)

    canevas.after(2, mouvement)
    return

# Placement des composants
canevas.grid()
mouvement()

# Boucle infinie
fenetre.mainloop()