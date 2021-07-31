import pypokedex
import PIL.Image, PIL.ImageTk
import urllib3
from io import BytesIO
from tkinter import *


def search_pokemon():

    pokemon = pypokedex.get(name=pokemon_entry.get(1.0,"end-1c"))

    http = urllib3.PoolManager()
    response = http.request('Get', pokemon.sprites.front.get('default'))
    
    image = PIL.Image.open(BytesIO(response.data))

    image = PIL.ImageTk.PhotoImage(image)
    pokemon_img.config(image=image)
    pokemon_img.image = image 

    pokemon_info['text'] =f"No: {pokemon.dex} , Name: {pokemon.name}".title()
    pokemon_types['text']= "Type: " + " & ".join([t for t in pokemon.types]).title()
    pokemon_hw['text'] = f"Height: {pokemon.height}dm , Weight: {pokemon.weight}hg"
    

win = Tk()
win.title("Pokdex")
win.geometry("400x400")

label_id_name = Label(win, text="Enter ID or Name")
label_id_name.pack(padx=10, pady=10)


pokemon_entry = Text(win, height=1, width=20,)
pokemon_entry.pack(padx=10, pady=10)

search_btn = Button(win, text="Search", command=search_pokemon).pack()


pokemon_info = Label(win, text="")
pokemon_info.pack(padx=10, pady=10)

pokemon_hw = Label(win)
pokemon_hw.pack(padx=10,pady=10)

pokemon_types = Label(win)
pokemon_types.pack(padx=10, pady=10)

pokemon_img = Label(win)
pokemon_img.pack(padx=10, pady=10)

 
win.mainloop()