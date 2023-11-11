import os 
import time

# Siia läheb exceli fail sisselugemiseks, loend, mis soovitab kasutajale eelistuste põhjal laule
song_list = [
    "Song 1",
    "Song 2",
    "Song 3",
    "Song 4",
    "Song 5"
]

current_song_index = 0
liked_songs = [] # Siia vaja lisada exceli faili sissekirjutamine, ehk iga meeldivaks pandud laul
# läheb kasutajale soovituste loomiseks loendisse

while True:
    os.system("cls" if os.name == "nt" else "clear")  # Kui käivitada, siis teeb terminali tühjaks
    current_song = song_list[current_song_index]
    
    print("Currently playing: ", current_song)
    print("Commands: (l)ike, (s)kip, (q)uit")

    user_input = input("Enter a command: ").lower()

    if user_input == "l":
        liked_songs.append(current_song)
        print("Liked: ", current_song)
        time.sleep(2)
        current_song_index = (current_song_index + 1) % len(song_list)
    elif user_input == "s":
        current_song_index = (current_song_index + 1) % len(song_list) # Uuendab mängitava laulu indeksit
        # ja käib läbi listi kuni otsa saab ning hakkab algusest pihta
        # % arvutab allesjäänud listi pikkuse
    elif user_input == "q":
        break

   
