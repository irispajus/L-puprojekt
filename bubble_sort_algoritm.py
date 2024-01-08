import pandas as pd

exceli_asukoht_PCs = 'C:/Users/irispajus/Desktop/PY/andmebaas.xlsx'

df = pd.read_excel(exceli_asukoht_PCs)

kaalupunktide_sorteerimine = 'kaalupunktid'

# bubble sortimine
n = len(df)
for i in range(n):
    for j in range(0, n-i-1):
        if pd.isna(df.loc[j, kaalupunktide_sorteerimine]) or (pd.notna(df.loc[j+1, kaalupunktide_sorteerimine]) and df.loc[j, kaalupunktide_sorteerimine] > df.loc[j+1, kaalupunktide_sorteerimine]):
            # võtab endaga kaasta mitte ainult kaalupunktid :) vaid ka muu rea väärtuse
            df.iloc[j], df.iloc[j+1] = df.iloc[j+1].copy(), df.iloc[j].copy()

df.to_excel('C:/Users/irispajus/Desktop/PY/andmebaas_sorteeritud.xlsx', index=False)

# happy learning at https://pandas.pydata.org/docs/reference/frame.html :)))

