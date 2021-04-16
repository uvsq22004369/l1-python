###################################################
# Groupe BI: 1
# Mathieu LAM
# Océane MACHADO
# Aurélie ALVET
# Timothé PEYREIGNE
# Thushanth JEYAKANTHN
# Merbah Yanis
# https://github.com/uvsq22004307/projet_incendie
###################################################



#import des librairies

import tkinter as tk
root = tk.Tk()
root.title("Projet Robot Ricochet")

grid = robot_rico(root)
grid.load(initial_values=G)
 
grid.pack(fill='both')
grid.update() # update grid to get real position from xxx_bbox
grid.focus_set()



tk.mainloop root








