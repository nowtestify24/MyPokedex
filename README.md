## MyPokedex

# Overview
MyPokedex is a Python-based graphical user interface (GUI) application that allows users to search and explore Pokémon information. Built using the tkinter library for the GUI, pypokedex to fetch Pokémon data, and pygame for music playback, this application provides a comprehensive and interactive experience for Pokémon enthusiasts.

# Features
Search by ID or Name: Enter a Pokémon ID or name to display its image, dex number, name, and types.

- Navigation: Use the Previous and Next buttons to browse through Pokémon sequentially.

- Random Pokémon: Generate a random Pokémon entry.

- Music Toggle: Toggle background music on or off.

- Main Menu Navigation: Navigate back to the main menu from the Pokedex screen.

# Requirements
- Python 3.x
- pypokedex library
- Pillow library
- requests library
- pygame library

# Install the necessary libraries using:
pip install pypokedex pillow requests pygame

# Usage
- Run the Program: Start the application by running the script.
- Main Menu: Use the main menu to begin the Pokedex or toggle music.

# Pokedex Screen:

- Search: Enter a Pokémon ID or name and press Enter or click Load.

- Navigation: Use Previous and Next to browse Pokémon.

- Random: Click the Random button to display a random Pokémon.

- Music: Use the Music Toggle button in the main menu to manage background music.

# Music Playback
To enjoy background music while using the Pokedex:

- Prepare your music file: Place an MP3 file named PokemonCenter.mp3 in a designated directory on your computer.

- Edit the file path: Ensure the path in the script points to the location of your music file.

- Toggle Music: Use the "Toggle Music" button in the main menu to play or stop the music.

## Code Overview

# Main Components
- Main Menu: Provides options to begin the Pokedex, toggle music, or exit the application.
- Pokedex Screen: Displays Pokémon information with options to load by ID/name, navigate, or get a random entry.
- Error Handling: If a Pokémon is not found, a blank image and error message are displayed.

# Functions
- load_pokemon_by_dex(dex): Fetches and displays Pokémon information by dex number.

- load_pokemon_by_name(name): Fetches and displays Pokémon information by name.

- load_pokemon(): Determines the type of search (ID or name) and fetches the Pokémon.

- quit(): Exits the application.

- randomPokemon(): Generates and displays a random Pokémon.

- next_pokemon(): Displays the next Pokémon in the dex.

- prev_pokemon(): Displays the previous Pokémon in the dex.

- toggle_music(): Toggles the background music on or off.

- show_main_menu(): Displays the main menu.

- show_pokedex(): Displays the Pokedex screen.

- bind_enter_key(): Binds the Enter key to initiate a Pokémon search.

# Key Bindings
- The Enter key is bound to initiate a search for Pokémon by ID or name. The binding is maintained across various states and actions in the application.

# Known Issues
- Ensure the correct installation of required libraries.
- Handle edge cases where Pokémon data might not be fetched properly. Specifically Pokedex entry 668

# Credits
Special thanks to the developers of the pypokedex, Pillow, and pygame libraries.


