import tkinter as tk

monDessin = tk.Tk()
monDessin.config(bg="#252526")
monDessin.title("Mon dessin")
choisirCouleur = tk.Button(monDessin, text="choisir un couleur", bg='black',
                           fg='white', bd=0
                           )
cercle = tk.Button(monDessin, text="Cercle", bg='black', fg='white', bd=0)
carre = tk.Button(monDessin, text="Carré", bg='black', fg='white', bd=0)
croix = tk.Button(monDessin, text="Croix", bg='black', fg='white', bd=0)
canva = tk.Canvas(monDessin, bg='black', height=256, width=256, bd=0)

choisirCouleur.grid(row=0, column=1, pady=2, padx=2)
cercle.grid(row=1, column=0, padx=5, pady=5)
carre.grid(row=2, column=0, padx=5, pady=5)
croix.grid(row=3, column=0, padx=5, pady=5)
canva.grid(row=1, column=1, rowspan=3, pady=2, padx=2)

monDessin.mainloop()
