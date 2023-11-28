import random
import pandas as pd

fail = "andmebaas.xlsx"

df = pd.read_excel(fail)

# ridade defineerimine
pealkiri = 0
artist = 1
zanr = 2
aasta = 3

# mitu lugu (rida) on failis
lugude_arv = df.shape[0]

print(lugude_arv)

# programm genereerib suvalise numbri, millisel real olevat lugu esimesena kuulajale pakub
suvaline_lugu = random.randint(0, lugude_arv)

kasutaja_valik = "n"

while kasutaja_valik != "q":
    # programm prindib välja suveline_lugu reale vastava loo
    for i in range(1, 5):
        lugu = df.cell(row = suvaline_lugu, column = i)
        kaalupunktid = 1
        sama_vaartus = df[df[column] == lugu.value]
        df.to_excel(fail, index=False)
        print(lugu.value, end = " ")
        
    kasutaja_valik = input("\nn(ext) or q(uit): ")
    
    
    
    
    
    

print("Program is closed.")




