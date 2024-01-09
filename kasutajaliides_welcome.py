import random
import tkinter as tk
from tkinter import messagebox
import pandas as pd

class WelcomeWindow:
    def __init__(self, master, kasutajanimi):
        self.master = master
        master.title("Tere tulemast, {}".format(kasutajanimi))

        # Aknasuuruse määramine
        master.geometry("300x200")

        # Laadime andmed failist
        fail = "andmebaas.xlsx"
        self.df = pd.read_excel(fail)

        # ridade defineerimine
        self.pealkiri = 0
        self.artist = 1

        # mitu lugu (rida) on failis
        self.lugude_arv = self.df.shape[0]

        # Nuppude konteiner
        button_container = tk.Frame(self.master)
        button_container.pack(pady=10)

        # Like, Skip ja Sulge nupud
        tk.Button(button_container, text="Like", command=self.like_action).pack(side=tk.LEFT, padx=10)
        tk.Button(button_container, text="Skipp", command=self.skipp_action).pack(side=tk.LEFT, padx=10)
        tk.Button(button_container, text="Sulge", command=self.master.destroy).pack(side=tk.RIGHT, padx=10)

        # Alusta esimese looga
        self.current_song_index = -1
        self.show_random_song()

    def show_random_song(self):
        # Kontrolli, kas kõik lood on läbi käidud, alusta uuesti
        if self.current_song_index == self.lugude_arv - 1:
            self.current_song_index = -1

        self.current_song_index += 1
        lugu_pealkiri = self.df.iloc[self.current_song_index, self.pealkiri]
        lugu_artist = self.df.iloc[self.current_song_index, self.artist]

        # Eemalda eelmine artist ja laul
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        tk.Label(self.master, text=f"Artist: {lugu_artist}").pack(pady=10)
        tk.Label(self.master, text=f"Laul: {lugu_pealkiri}").pack(pady=5)

    def like_action(self):
        # Tee midagi like nupule vajutamisel
        messagebox.showinfo("Tegevus", "Like!")
        # Näita uut lugu
        self.show_random_song()

    def skipp_action(self):
        # Tee midagi skipp nupule vajutamisel
        messagebox.showinfo("Tegevus", "Skipp!")
        # Näita uut lugu
        self.show_random_song()
