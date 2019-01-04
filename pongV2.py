from tkinter import *
from random import *
from time import *
from tkinter.colorchooser import *

# Dimensions
hauteur = 500
largeur = 900

# Scores
score1 = 0
score2 = 0

# Status du jeu
game_is_launch = False

# Creation balle
balle_x0 = 440
balle_x1 = balle_x0 + 20
balle_y0 = 240
balle_y1 = balle_y0 + 20
vx_balle = 5.2
vy_balle = 1

# Creation raquette1
raq1_x0 = 10
raq1_x1 = 22
raq1_y0 = 200
raq1_y1 = 300

# Creation raquette2
raq2_x0 = largeur - 20
raq2_x1 = raq2_x0 + 12
raq2_y0 = 200
raq2_y1 = 300

# Pour background sur mesure
def background_color():
    color = askcolor()
    color = color[1]
    print(color)
    color = str(color)
    print(color)
    return color

color = background_color()

# Creation des composants
fenetre = Tk()
fenetre.title('Pong - Thibault Feugere')
canevas = Canvas(fenetre, width=largeur, height=hauteur, bg=color)

# Pour eviter le bug OUT OF RANGE
balle = canevas.create_oval(balle_x0, balle_y0, balle_x1, balle_y1, fill = "red")

# Empeche de redimenssionner la fenetre
fenetre.resizable(False,False)

# Definition du menu
def menu():
    canevas.delete(ALL)
    canevas.create_text(450, 200, fill = "white", font = ("Roboto", 70), text = "ACCUEIL")

    # Creation des boutons
    quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
    accueil = Button(fenetre, text = "Accueil", command = menu)
    jouer = Button(fenetre, text="Jouer", command = jeu)

    # Placement des boutons
    accueil.grid(column = 0, pady = 15)
    jouer.grid()
    quitter.grid(row = 1, column = 2)

# Definition du jeu
def jeu():
    canevas.delete(ALL)

    # Creation de la balle
    balle = canevas.create_oval(balle_x0, balle_y0, balle_x1, balle_y1, fill = "white")

    # Creation des raquettes
    raquette1 = canevas.create_rectangle(raq1_x0, raq1_y0, raq1_x1, raq1_y1, fill = "white")
    raquette2 = canevas.create_rectangle(raq2_x0, raq2_y0, raq2_x1, raq2_y1, fill = "white")

    # Delimitation
    barre_verticale = canevas.create_line((largeur/2), 0, (largeur/2), hauteur, fill="red", dash=(2,2))

    # Definition de la fonction start / pause
    def launch():
        global game_is_launch
        game_is_launch = True

    def pause():
        global game_is_launch
        game_is_launch = False

    # Menu footer
    start = Button(fenetre, text="Commencer", command=launch)
    pause = Button(fenetre, text="Pause", command=pause)

    # Placement du menu
    start.grid(row = 1,column = 1, ipadx = 30)
    pause.grid(row = 2, column = 1, pady = 15)

    def z_key(event):
        canevas.move(raquette1,0,-15)
    def s_key(event):
        canevas.move(raquette1,0,15)
    def up_key(event):
        canevas.move(raquette2,0,-15)
    def down_key(event):
        canevas.move(raquette2,0,15)

    # Detection de touches pressees
    canevas.bind_all('z', z_key)
    canevas.bind_all('s', s_key)
    canevas.bind_all('<Up>', up_key)
    canevas.bind_all('<Down>', down_key)

    # Affichage initial des scores
    score_1 = canevas.create_text(370, 20, text="Joueur 1 : "+str(score1), fill="white", font="Verdana 11")
    score_2 = canevas.create_text(530, 20, text="Joueur 2 : "+str(score2), fill="white", font="Verdana 11")

    def mouvement():
        global balle_x0, balle_y0, balle_x1, balle_y1, vx_balle, vy_balle, score1, score2, score_1, score_2

        canevas.move(balle, vx_balle, vy_balle)

        if canevas.coords(balle)[2] > largeur:
            global score_1
            vx_balle = -(vx_balle)
            score1 += 1
            print(score1)
            #canevas.delete(score_1)
            score_1 = canevas.create_text(370, 20, text="Joueur 1 : "+str(score1), fill="white", font="Verdana 11")
            if score1 == 3:
                victoire1()

        elif canevas.coords(balle)[0] < 0:
            global score_2
            vx_balle = -(vx_balle)
            score2 += 1
            print(score2)
            #canevas.delete(score_2)
            score_2 = canevas.create_text(530, 20, text="Joueur 2 : "+str(score2), fill="white", font="Verdana 11")
            if score2 == 3:
                victoire2()

        elif canevas.coords(balle)[3] > hauteur or canevas.coords(balle)[1] < 0 :
            vy_balle = -(vy_balle)

        elif canevas.coords(balle)[2] > canevas.coords(raquette2)[0] and canevas.coords(balle)[3] > canevas.coords(raquette2)[1] and canevas.coords(balle)[1] < canevas.coords(raquette2)[3] or canevas.coords(balle)[0] < canevas.coords(raquette1)[2] and canevas.coords(balle)[3] > canevas.coords(raquette1)[1] and canevas.coords(balle)[1] < canevas.coords(raquette1)[3]:
            vx_balle = -(vx_balle)
        canevas.after(20, mouvement)
    mouvement()

# Definition fin du jeu
def victoire1():
    canevas.delete(ALL)
    canevas.create_text(largeur / 2, 300, fill = "white", font = ("Roboto", 50), text = "JOUEUR 1 A GAGNE")

def victoire2():
    canevas.delete(ALL)
    canevas.create_text(largeur / 2, 300, fill = "white", font = ("Roboto", 50), text = "JOUEUR 2 A GAGNE")


# Placement des composants
canevas.grid(row = 0, columnspan = 3)
menu()

# Boucle infinie
fenetre.mainloop()