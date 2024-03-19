import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

# Début de votre code
x0 = CANVAS_WIDTH/2
x1 = CANVAS_WIDTH - x0
y0 = (100*CANVAS_HEIGHT)/CANVAS_WIDTH
y1 = CANVAS_HEIGHT - y0
canvas.create_line(x0, y0, x1, y1)
canvas.create_oval(x0 - 50, y0 + 50, x0 + 50, y0 - 50)
canvas.create_oval(x1 - 50, y1 - 50, x1 + 50, y1 + 50)
canvas.create_oval(x0 - 50, (y0 + y1) / 2 + 50, x1 + 50, (y0 + y1) / 2 - 50)
# Fin de votre code

canvas.grid()
root.mainloop()
