import pypokedex
import PIL
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import font
from io import BytesIO
from random import randint
import requests
import pygame

global current_pokemon_index, pokemon_image, pokemon_information, pokemon_types, text_id_name
def handle_enter_key(event):        #event handler for enter key
    load_pokemon()
    return 'break'  # Prevent default Text behavior
def load_pokemon_by_dex(dex):
    try:
        pokemon = pypokedex.get(dex=dex)
        response = requests.get(pokemon.sprites.front.get('default'))
        image = PIL.Image.open(BytesIO(response.content))           #get our pokemon image and resize it to fit properly
        image = image.resize((200, 200), PIL.Image.ANTIALIAS)
        pokeImage = PIL.ImageTk.PhotoImage(image)
        pokemon_image.config(image=pokeImage)
        pokemon_image.image = pokeImage
        pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())      #gather pokemon info from the API call
        pokemon_types.config(text=" - ".join([t.title() for t in pokemon.types]))
        global current_pokemon_index
        current_pokemon_index = pokemon.dex         #set our current dex entry used for navigation buttons
    except Exception as e:
        pokemon_information.config(text="Pokemon not found or an error occurred.")      #exception thrown when pokemon not found
        print(e)
    
def load_pokemon_by_name(name):
    global current_pokemon_index
    try:
        pokemon = pypokedex.get(name=name)
        response = requests.get(pokemon.sprites.front.get('default'))
        image = PIL.Image.open(BytesIO(response.content))
        image = image.resize((200, 200), PIL.Image.ANTIALIAS)
        pokeImage = PIL.ImageTk.PhotoImage(image)               #gather our pokemon information via name
        pokemon_image.config(image=pokeImage)                   #and set our image, name and type to be displayed
        pokemon_image.image = pokeImage
        pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
        pokemon_types.config(text=" - ".join([t.title() for t in pokemon.types]))
        current_pokemon_index = pokemon.dex
       
    except Exception as e:
        pokemon_information.config(text="Pokemon not found or an error occurred.")  #exception thrown when pokemon not found
        pokemon_types.config(text="")
        print(e)

def load_pokemon():
    name_or_id = text_id_name.get(1.0, "end-1c").lower()
    if name_or_id.isdigit():                #function to handle logic when user inputs dex number or a name
        load_pokemon_by_dex(int(name_or_id))
    else:
        load_pokemon_by_name(name_or_id)
    text_id_name.delete(1.0,tk.E)
    

def quit():
    window.destroy()                #exit function

def randomPokemon():
    randomNumber = randint(1, 1025)     #function used to give us a random pokemon
    load_pokemon_by_dex(randomNumber)

def next_pokemon():
    global current_pokemon_index
    current_pokemon_index = 1 if current_pokemon_index == 1025 else current_pokemon_index + 1
    load_pokemon_by_dex(current_pokemon_index)              #moves us forward in pokedex or back to 1 if we reach end
    text_id_name.delete(1.0, tk.END)  # Clear the text box

def prev_pokemon():
    global current_pokemon_index
    current_pokemon_index = 1025 if current_pokemon_index == 1 else current_pokemon_index - 1
    load_pokemon_by_dex(current_pokemon_index)          #moves us back in pokedex or to the end if we are at 1
    text_id_name.delete(1.0, tk.END)  # Clear the text box
def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.load("C:/Users/Ross/Desktop/PythonStuff/PokemonMusic/PokemonCenter.mp3")
        pygame.mixer.music.play(-1)

def show_main_menu():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    main_menu_frame = tk.Frame(window, bg="#ADD8E6")
    main_menu_frame.pack(expand=True)
    #create title frame
    title_label = tk.Label(main_menu_frame, text="Welcome to MyPokedex!", font=("Arial", 24, "bold"), bg="#ADD8E6", fg="#333")
    title_label.pack(pady=20)
    #create begin button that will show the pokedex
    btn_begin = tk.Button(main_menu_frame, text="Begin", command=show_pokedex, bg="#48D1CC", fg="#FFF", relief="raised", bd=3)
    btn_begin.config(font=custom_font)
    btn_begin.pack(pady=10)
    #toggle music button to turn music on or off
    btn_toggle_music = tk.Button(main_menu_frame, text="Toggle Music", command=toggle_music, bg="#FFA500", fg="#FFF", relief="raised", bd=3)
    btn_toggle_music.config(font=custom_font)
    btn_toggle_music.pack(pady=10)

    btn_exit = tk.Button(main_menu_frame, text="Exit", command=quit, bg="#FF6347", fg="#FFF", relief="raised", bd=3)
    btn_exit.config(font=custom_font)
    btn_exit.pack(pady=10)
def show_pokedex():
    # Clear the window
    for widget in window.winfo_children():      #clear the window
        widget.destroy()

    custom_font = tk.font.Font(family="Red Hat Mono", size=12, weight="bold")
    title_frame = tk.Frame(window, bg="#ADD8E6")            #declare title frame and lable
    title_frame.pack(pady=10)

    title_label = tk.Label(title_frame, text="Kane's Pokedex", font=("Arial", 24, "bold"), bg="#ADD8E6", fg="#333")
    title_label.pack()

    back_button = tk.Button(window, text="Back", command=show_main_menu, bg="#FF6347", fg="#FFF", relief="raised", bd=3)
    back_button.config(font=custom_font)
    back_button.place(relx=0.0, rely=0.0, anchor="nw")
    #frame used to display our pokemon sprite
    image_frame = tk.Frame(window, bg="#ADD8E6")
    image_frame.pack(pady=10)

    global pokemon_image
    pokemon_image = tk.Label(image_frame, bg="#ADD8E6")     #pokemon image widget
    pokemon_image.pack()

    info_frame = tk.Frame(window, bg="#ADD8E6")
    info_frame.pack(pady=10)

    global pokemon_information
    pokemon_information = tk.Label(info_frame, bg="#ADD8E6", fg="#333")
    pokemon_information.config(font=custom_font)        #pokemon information for name widget
    pokemon_information.pack(padx=10, pady=5)

    global pokemon_types
    pokemon_types = tk.Label(info_frame, bg="#ADD8E6", fg="#333")
    pokemon_types.config(font=custom_font)
    pokemon_types.pack(padx=10, pady=5)             #pokemon type widget
     #frame for input handling and
    input_frame = tk.Frame(window, bg="#ADD8E6")
    input_frame.pack(pady=10)          
    #label widet for user input prompt, either Dex number or name
    label_id_name = tk.Label(input_frame, text="Enter ID or Name", bg="#ADD8E6", fg="#333")
    label_id_name.config(font=custom_font)
    label_id_name.pack(side=tk.LEFT, padx=5)
    #input box widget that handles user input if enter key is pressed 
    global text_id_name
    text_id_name = tk.Text(input_frame, height=1, width=20)
    text_id_name.config(font=custom_font)
    text_id_name.pack(side=tk.LEFT, padx=5)
    text_id_name.bind("<Return>", handle_enter_key)  # Bind the Enter key
    #load button to be used instead of enter key
    btn_load = tk.Button(input_frame, text="Load", command=load_pokemon, bg="#48D1CC", fg="#FFF", relief="raised", bd=3)
    btn_load.config(font=custom_font)
    btn_load.pack(side=tk.LEFT, padx=5)

    nav_frame = tk.Frame(window, bg="#ADD8E6")
    nav_frame.pack(pady=10)
    #previous button to go to previous entries of pokedex
    btn_prev = tk.Button(nav_frame, text="Previous", command=prev_pokemon, bg="#48D1CC", fg="#FFF", relief="raised", bd=3)
    btn_prev.config(font=custom_font)
    btn_prev.pack(side=tk.LEFT, padx=10)
    #next button to go forward in the pokedex
    btn_next = tk.Button(nav_frame, text="Next", command=next_pokemon, bg="#48D1CC", fg="#FFF", relief="raised", bd=3)
    btn_next.config(font=custom_font)
    btn_next.pack(side=tk.LEFT, padx=10)

    # New frame for the Random button
    random_frame = tk.Frame(window, bg="#ADD8E6")
    random_frame.pack(pady=10)
    #button that gives us a random pokemon
    btn_random = tk.Button(random_frame, text="Random Pokemon", command=randomPokemon, bg="#FF1493", fg="#FFF", relief="raised", bd=3)
    btn_random.config(font=("Red Hat Mono", 14, "bold"))  # Increase the font size
    btn_random.pack(pady=10)

   
    # Load Bulbausaur as the first Pokémon
    load_pokemon_by_dex(1)


#window declaration
window = tk.Tk()    
window.geometry("600x600")
window.title("Kane's Pokedex")
window.config(padx=20, pady=20, bg="#ADD8E6")  # Light blue background
window.minsize(600, 600)  # Minimum size: 600x600 pixels
pygame.mixer.init()
#start playing the music and declare our font
toggle_music()
custom_font = tk.font.Font(family="Red Hat Mono", size=12, weight="bold")
#display the main menu
show_main_menu()
window.mainloop()
