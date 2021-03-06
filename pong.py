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

# Creation de la balle
balle_x0 = 440
balle_x1 = 460
balle_y0 = 240
balle_y1 = 260
balle_v_x = 4.2
balle_v_y = 1.2
balle = canevas.create_oval(balle_x0, balle_y0, balle_x1, balle_y1, fill="white", width=0, state="disabled")

# Creation raquette du joueur un
raq1_x0 = 5
raq1_x1 = 20
raq1_y0 = 215
raq1_y1 = 285
raq1_v_y = 18
raquette1 = canevas.create_rectangle(raq1_x0, raq1_y0, raq1_x1, raq1_y1, fill="white", width=0, state="disabled")

# Creation raquette du joueur deux
raq2_x0 = 880
raq2_x1 = 895
raq2_y0 = 215
raq2_y1 = 285
raq2_v_y = 18
raquette2 = canevas.create_rectangle(raq2_x0, raq2_y0, raq2_x1, raq2_y1, fill="white", width=0, state="disabled")

### Fonctions ###

# Fonction mouvement infini
def mouvement():
    global balle_x0, balle_y0, balle_v_x, balle_v_y, balle_x1, balle_y1, game_is_launch
    if game_is_launch == True:
        balle_x0 += balle_v_x
        balle_y0 += balle_v_y
        canevas.coords(balle, balle_x0, balle_y0, (balle_x0 + 20), (balle_y0 + 20))
    #if (balle_y0 < raq1_y1) and (balle_y1 > raq1_y0) and (balle_x0 < raq1_x1):
    if canevas.coords(raquette2)[1] <= canevas.coords(balle)[3] <= canevas.coords(raquette2)[3] and canevas.coords(balle)[2] == canevas.coords(raquette2)[0] or canevas.coords(raquette1)[1] <= canevas.coords(balle)[3] <= canevas.coords(raquette2)[3] and canevas.coords(balle)[0] == canevas.coords(raquette1)[2]:
        balle_v_x = -(balle_v_x)
    canevas.after(2, mouvement)
    return

def rebond_raquettes():
    global balle_v_x, balle_v_y
    #if (canevas.coords(balle)[3]>canevas.coords(raquette1)[1]) and (canevas.coords(balle)[0]<canevas.coords(raquette1)[2]) and (canevas.coords(balle)[2]>canevas.coords(raquette1)[0]):
        #balle_v_x = -(balle_v_x)
    pass
# Fonction de verification avec score
def verif_balle():
    global balle_x0, balle_y0, balle_x1, balle_y1, balle_v_x, balle_v_y, raq1_x0, raq1_y0, raq1_v_y, score1, score2, score_1, score_2, suppr_score_1, suppr_score_2
    if balle_x0 + 20 > largeur:
        balle_v_x = -(balle_v_x)
        score1 += 1
        suppr_score_1 = canevas.delete(score_1)
        score_1 = canevas.create_text(370, 20, text="Joueur 1 : "+str(score1), fill="white", font="Verdana 11")
    elif balle_x0 < 0:
        balle_v_x = -(balle_v_x)
        score2 += 1
        suppr_score_2 = canevas.delete(score_2)
        score_2 = canevas.create_text(530, 20, text="Joueur 2 : "+str(score2), fill="white", font="Verdana 11")
    elif balle_y0 + 20 > hauteur or balle_y0 < 0:
        balle_v_y = -(balle_v_y)
    canevas.after(2, verif_balle)

# Fonctions de commande
def z_key(event):
    global raq1_x0, raq1_y0, raq1_v_y, game_is_launch
    if game_is_launch == True:
        raq1_y0 -= raq1_v_y
        canevas.coords(raquette1, raq1_x0, raq1_y0, (raq1_x0 + 14), (raq1_y0 + 70))
        return raq1_y0

def s_key(event):
    global raq1_x0, raq1_y0, raq1_v_y, game_is_launch
    if game_is_launch == True:
        raq1_y0 += raq1_v_y
        canevas.coords(raquette1, raq1_x0, raq1_y0, (raq1_x0 + 14), (raq1_y0 + 70))

def up_key(event):
    global raq2_x0, raq2_y0, raq2_v_y, game_is_launch
    if game_is_launch == True:
        raq2_y0 -= raq2_v_y
        canevas.coords(raquette2, raq2_x0, raq2_y0, (raq2_x0 - 14), (raq2_y0 + 70))

def down_key(event):
    global raq2_x0, raq2_y0, raq2_v_y, game_is_launch
    if game_is_launch == True:
        raq2_y0 += raq2_v_y
        canevas.coords(raquette2, raq2_x0, raq2_y0, (raq2_x0 - 14), (raq2_y0 + 70))

# Definition affichage menu principal
def menu_principal():
    canevas.delete(ALL)

# Definition de la fonction start / pause
def launch():
    global game_is_launch
    game_is_launch = True

def pause():
    global game_is_launch
    game_is_launch = False

# Definition affichage vainceur
def perdu():
    if score1 == 10:    
        canevas.delete(ALL)
        canevas.create_text(largeur / 2, 300, fill = "white", font = ("Roboto", 55), text = "Le joueur 1 a gagn??")

# Creation du menu
start = Button(fenetre, text="Commencer", command=launch)
pause = Button(fenetre, text="Pause", command=pause)
quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
accueil = Button(fenetre, text = "Accueil", command = menu_principal)

# Placement des composants
canevas.grid(row = 0, columnspan = 3)

accueil.grid(column = 0, pady = 15)
start.grid(row = 1,column = 1, ipadx = 30)
pause.grid(row = 2, column = 1, pady = 15)
quitter.grid(row = 1, column = 2)

rebond_raquettes()
mouvement()
verif_balle()

score_1 = canevas.create_text(370, 20, text="Joueur 1 : "+str(score1), fill="white", font="Verdana 11")
score_2 = canevas.create_text(530, 20, text="Joueur 2 : "+str(score2), fill="white", font="Verdana 11")

# Detection de touches pressees
canevas.bind_all('z', z_key)
canevas.bind_all('s', s_key)
canevas.bind_all('<Up>', up_key)
canevas.bind_all('<Down>', down_key)

# Boucle infinie
fenetre.mainloop()