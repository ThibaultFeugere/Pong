from tkinter import *
from random import *
from time import *

# Dimensions
hauteur = 500
largeur = 900

# Scores
score1 = 0
score2 = 0

# Status du jeu
game_is_launch = False

# Creation des composants
fenetre = Tk()
fenetre.title('Pong - Thibault Feugère')
canevas = Canvas(fenetre, width=largeur, height=hauteur, bg='black')

# Delimitation
barre_verticale = canevas.create_line((largeur/2), 0, (largeur/2), hauteur, fill="red", dash=(2,2))

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
raq1_v_y = 5
raquette1 = canevas.create_rectangle(raq1_x0, raq1_y0, (raq1_x0 + 14), (raq1_y0 + 70), fill="white", width=0, state="disabled")

# Creation raquette du joueur deux
raq2_x0 = largeur - 4
raq2_y0 = 215
raq2_v_y = 5
raquette2 = canevas.create_rectangle(raq2_x0, raq2_y0, (raq2_x0 - 14), (raq2_y0 + 70), fill="white", width=0, state="disabled")

### Fonctions ###

# Fonction mouvement infini
def mouvement():
    global balle_x0, balle_y0, balle_v_x, balle_v_y, score1, score2, game_is_launch
    '''if game_is_launch == True:'''
    balle_x0 += balle_v_x
    balle_y0 += balle_v_y

    canevas.coords(balle, balle_x0, balle_y0, (balle_x0 + 20), (balle_y0 + 20))
    canevas.after(2, mouvement)
    return

# Fonction de verification avec score
def verif():
    global balle_x0, balle_y0, balle_v_x, balle_v_y, raq1_x0, raq1_y0, raq1_v_y, score1, score2
    if (balle_x0 + 20) > largeur:
        balle_v_x = -(balle_v_x)
        score1 += 1
    elif balle_x0 < 0:
        balle_v_x = -(balle_v_x)
        score2 += 1
    elif (balle_y0 + 20) > hauteur:
        balle_v_y = -(balle_v_y)
    elif balle_y0 < 0:
        balle_v_y = -(balle_v_y)
    canevas.after(2, verif)

# Fonctions de commande
def z_key(event):
    global raq1_x0, raq1_y0, raq1_v_y
    raq1_y0 -= raq1_v_y
    canevas.coords(raquette1, raq1_x0, raq1_y0, (raq1_x0 + 14), (raq1_y0 + 70))

def s_key(event):
    global raq1_x0, raq1_y0, raq1_v_y
    raq1_y0 += raq1_v_y
    canevas.coords(raquette1, raq1_x0, raq1_y0, (raq1_x0 + 14), (raq1_y0 + 70))

def up_key(event):
    global raq2_x0, raq2_y0, raq2_v_y
    raq2_y0 -= raq2_v_y
    canevas.coords(raquette2, raq2_x0, raq2_y0, (raq2_x0 - 14), (raq2_y0 + 70))

def down_key(event):
    global raq2_x0, raq2_y0, raq2_v_y
    raq2_y0 += raq2_v_y
    canevas.coords(raquette2, raq2_x0, raq2_y0, (raq2_x0 - 14), (raq2_y0 + 70))

# Definition de la fonction start / pause
'''
def launch():
    global game_is_launch
    game_is_launch = True
    return game_is_launch
'''

# Creation du menu
#start = Button(fenetre, text="Commencer", command=launch)
quitter = Button(fenetre, text="Quitter", command=fenetre.quit)

# Placement des composants
canevas.grid()
#start.grid()
quitter.grid()
mouvement()
verif()

canevas.bind_all('z', z_key)
canevas.bind_all('s', s_key)
canevas.bind_all('<Up>', up_key)
canevas.bind_all('<Down>', down_key)

# Boucle infinie
fenetre.mainloop()

print('''Le joueur 1 a''', score1, '''point(s)''')
print('''Le joueur 2 a''', score2, '''point(s)''')
