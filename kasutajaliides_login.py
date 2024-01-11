#https://www.w3schools.com/python/gloss_python_class_init.asp

import tkinter as tk
from tkinter import messagebox
import pandas as pd
from kasutajaliides_welcome import WelcomeWindow  # Importib WelcomeWindow klassi teisest failist
import os
import random

class LoginWindow:
    # Konstruktor (__init__) initsialiseerib akna ja määrab sellele pealkirja
    def __init__(self, master):
        self.master = master # Peamine (main) aken
        master.title("Sisselogimise aken")

        # Aknasuuruse määramine
        master.geometry("270x300")

        # Kutsun meetodit akna loomiseks
        self.loo_graafiline_element()

    # Meetod, mis loob ja paigutab graafilised elemendid peamisse (main) aknasse
    def loo_graafiline_element(self):

        # Siltide ja sisendite kujundamine kasutajanime jaoks
        tk.Label(self.master, text="Kasutajanimi:").pack(pady=10)
        self.kasutajanimi_entry = tk.Entry(self.master)
        self.kasutajanimi_entry.pack(pady=10)

        # Siltide ja sisendite kujundamine parooli jaoks
        tk.Label(self.master, text="Parool:").pack(pady=10)
        self.parool_entry = tk.Entry(self.master, show="*")
        self.parool_entry.pack(pady=10)

        # Loon nupud konto loomiseks ja sisselogimiseks
        tk.Button(self.master, text="Loo konto", command=self.loo_kasutaja).pack(pady=10)
        tk.Button(self.master, text="Logi sisse", command=self.kontrolli_sisselogimist).pack(pady=20)

    # Meetod, mis kutsutakse esile kui kasutaja vajutab "Loo konto" nuppu
    def loo_kasutaja(self):

        # Kasutajanimi ja parool võetakse peamise akna sisestusväljadest
        kasutajanimi = self.kasutajanimi_entry.get()
        parool = self.parool_entry.get()

        if kasutajanimi and parool:

            # Kontrollin esmalt kas kasutajanimi on juba kasutusel ehk olemas exceli failis
            # Kui olemas, annab vastava veateate
            if self.kasutajanimi_olemas_failis(kasutajanimi):
                messagebox.showerror("Viga", "Kasutajanimi {} on juba kasutusel. Palun vali uus kasutajanimi.".format(kasutajanimi))
            
            # Kui sisestatud kasutajanimi pole kasutusel, salvestatakse see exceli faili ja luuakse konto
            else:
                self.salvesta_excelisse(kasutajanimi, parool)
                messagebox.showinfo("Konto loodud", "Kasutaja {} konto on loodud edukalt.".format(kasutajanimi))

                # Tühjendan sisestusväljad peamises aknas
                self.tuhjenda_sisend()
        else:
            messagebox.showerror("Viga", "Palun sisesta nii kasutajanimi kui ka parool.")

    # Meetod, mis kontrollib kas kasutajanimi on juba kasutusel
    # Kutsutakse esile loo_kasutaja ja kontrolli_sisselogimist funktsioonis
    def kasutajanimi_olemas_failis(self, kasutajanimi):
        try:
            df = pd.read_excel(exceli_asukoht)
            return kasutajanimi in df["Kasutajanimi"].values
        except FileNotFoundError:
            return False

    # Meetod, mis kutsutakse esile kui kasutaja vajutab "Logi sisse" nuppu
    def kontrolli_sisselogimist(self):

        # Kasutajanimi ja parool võetakse peamise akna sisestusväljadest
        sisestatud_kasutajanimi = self.kasutajanimi_entry.get()
        sisestatud_parool = str(self.parool_entry.get()).strip()

        # Kontrollin esmalt kas kasutajanimi on olemas kasutajad.xlsx failis
        if self.kasutajanimi_olemas_failis(sisestatud_kasutajanimi):

            # Kui on olemas, leian selle failist üles ja faili andmed laaditakse DataFrame'i
            df = pd.read_excel(exceli_asukoht)

            # Võrdlen sisestusväljadest saadud andmeid failis olevatega
            if df.loc[df['Kasutajanimi'] == sisestatud_kasutajanimi, 'Parool'].values[0] == sisestatud_parool:
                messagebox.showinfo("Sisselogimine õnnestus", "Tere tulemast, {}".format(sisestatud_kasutajanimi))
                
                # Meetod realiseerub kui sisestusväljades olevad andmed on võrdsed tabelis olevatega
                self.edukas_sisselogimine()
            
            # Kui parool ei ole võrdne aga kasutajanimi on, siis väljastatakse vastav veateade
            else:
                messagebox.showerror("Sisselogimine ebaõnnestus", "Vigane parool")
        # Kasutajanime ei leitud failist ja väljastatakse vastav veateade
        else:
            messagebox.showerror("Sisselogimine ebaõnnestus", "Kasutajanimi ei eksisteeri")

    # Meetod, mis kutsutakse esile kui kontrolli_sisselogimist funktsioonis saadakse väärtus True
    def edukas_sisselogimine(self):

        
        kasutajanimi = self.kasutajanimi_entry.get()

        # Generate a unique user identifier based on user input (you can modify this as needed)
        user_identifier = f'{kasutajanimi}'

        # Specify the path for the user's database
        user_db_path = os.path.join('C:/Users/eveli/OneDrive - Tallinna Tehnikaülikool/Algoritmid23/Projekt/UserDatabases/', f'{user_identifier}_andmebaas.xlsx')

        # Pass the user identifier and database path to the WelcomeWindow constructor
        uus_aken = tk.Tk()
        WelcomeWindow(uus_aken, user_identifier,user_db_path)
        
        
        
    # Meetod, mis salvestab kasutaja andmed Exceli faili
    def salvesta_excelisse(self, kasutajanimi, parool):
        try:
            # Püüab avada olemasoleva faili
            df = pd.read_excel(exceli_asukoht)

            # Kui õnnestub, siis lisatakse uue kasutaja andmed DataFrame'i
            new_users_df = pd.DataFrame([(kasutajanimi, parool)], columns=['Kasutajanimi', 'Parool'])
            df = pd.concat([df, new_users_df], ignore_index=True)
        except FileNotFoundError:
            # Kui ei õnnestu faili avada, luuakse uus DataFrame, mis hiljem salvestatakse uute loodud faili
            df = pd.DataFrame([(kasutajanimi, parool)], columns=['Kasutajanimi', 'Parool'])

        # Salvestab andmed Exceli faili
        df.to_excel(exceli_asukoht, index=False)

    def tuhjenda_sisend(self):
        self.kasutajanimi_entry.delete(0, tk.END)
        self.parool_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    exceli_asukoht = 'C:/Users/eveli/OneDrive - Tallinna Tehnikaülikool/Algoritmid23/Projekt/kasutajad.xlsx'
    app = LoginWindow(root)
    root.mainloop()