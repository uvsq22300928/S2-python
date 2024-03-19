import tkinter as tk
import random as random


def cercleAlea(canvas):
    taille1 = random.randint(10, 50)
    x1 = random.randint(taille1, 256-taille1)
    y1 = random.randint(taille1, 256-taille1)
    canvas.create_oval(x1 - taille1, y1 - taille1, x1 + taille1,
                       y1 + taille1, outline=couleur)


def carreAlea(canvas):
    taille1 = random.randint(10, 50)
    x1 = random.randint(taille1, 256-taille1)
    y1 = random.randint(taille1, 256-taille1)
    canvas.create_rectangle(x1 - taille1, y1 - taille1, x1 + taille1,
                            y1 + taille1, outline=couleur)


def croixAlea(canvas):
    # Récupérer les dimensions du Canvas
    largeur = canvas.winfo_width()
    hauteur = canvas.winfo_height()

    # Longueur aléatoire pour les bras de la croix
    longueur_bras = random.randint(10, min(largeur, hauteur) // 4)

    # Coordonnées aléatoires pour le centre de la croix
    x_centre = random.randint(longueur_bras, largeur - longueur_bras)
    y_centre = random.randint(longueur_bras, hauteur - longueur_bras)

    # Dessiner les lignes de la croix
    canvas.create_line(x_centre - longueur_bras, y_centre,
                       x_centre + longueur_bras, y_centre, fill=couleur)
    canvas.create_line(x_centre, y_centre - longueur_bras, x_centre,
                       y_centre + longueur_bras, fill=couleur)


def effacerCanvas(canvas):
    # Effacer tous les éléments dans le Canvas
    canvas.delete("all")


def choisirCouleur():
    global couleur
    couleur1 = input("Choisissez une couleur (white, black, red, green, blue,\
                      cyan, yellow): ").lower()
    if couleur1 in ['white', 'black', 'red', 'green', 'blue',
                    'cyan', 'yellow']:
        couleur = couleur1
    else:
        print("Couleur invalide. La couleur reste bleue.")
        couleur = "blue"


monDessin = tk.Tk()
monDessin.config(bg="#252526")
monDessin.title("Mon dessin")

couleur = "blue"

zoneDessin = tk.Canvas(monDessin, bg='black', height=256, width=256,
                       highlightthickness=0)
boutonChoisirCouleur = tk.Button(monDessin, text="choisir un couleur",
                                 bg='black', fg='white', bd=0,
                                 command=lambda: choisirCouleur())
effacer = tk.Button(monDessin, text="effacer le canvas", bg='black',
                    fg='white', bd=0,
                    command=lambda: effacerCanvas(zoneDessin))
boutonCercle = tk.Button(monDessin, text="Cercle", bg='black', fg='white',
                         bd=0, command=lambda: cercleAlea(zoneDessin))
boutonCarre = tk.Button(monDessin, text="Carré", bg='black', fg='white',
                        bd=0, command=lambda: carreAlea(zoneDessin))
boutonCroix = tk.Button(monDessin, text="Croix", bg='black', fg='white',
                        bd=0, command=lambda: croixAlea(zoneDessin))

boutonChoisirCouleur.grid(row=0, column=1, pady=2, padx=2)
boutonCercle.grid(row=1, column=0, padx=5, pady=5)
boutonCarre.grid(row=2, column=0, padx=5, pady=5)
boutonCroix.grid(row=3, column=0, padx=5, pady=5)
effacer.grid(row=0, column=2)
zoneDessin.grid(row=1, column=1, rowspan=3, columnspan=2, pady=2, padx=2)

monDessin.mainloop()
