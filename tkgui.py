import tkinter as tk
import time


#prepare window
root =tk.Tk()
root.title("sample_GUI")
root.geometry("2222x1080")

images=[
tk.PhotoImage(file='./image.png'),
tk.PhotoImage(file= './realtime0.png')
]
index = 0
"""while 1:
    
    key_in = input()
    if key_in =="end":
        break
    if (1037 - int(key_in)) % 3 == 0:
        index = 0
    else:
        index = 1
"""
canvas = tk.Canvas (width=2222,height=1080)
canvas.place(x=0,y=0)
canvas.create_image(0, 0, image=images[index], anchor=tk.NW,tag='p1')