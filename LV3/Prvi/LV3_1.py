import pandas as pd

mtcars = pd.read_csv("mtcars.csv")

mtcars['mass_kg'] = mtcars['wt'] * 0.453592

top5_potrosnja = mtcars.sort_values(by='mpg', ascending=False).head(5)
print("1. Kojih 5 automobila ima najveću potrošnju?")
print(top5_potrosnja[['car', 'mpg']])
print()

najmanja_potrosnja_8_cil = mtcars[mtcars['cyl'] == 8].sort_values(by='mpg').head(3)
print("2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?")
print(najmanja_potrosnja_8_cil[['car', 'mpg']])
print()

srednja_potrosnja_6_cil = mtcars[mtcars['cyl'] == 6]['mpg'].mean()
print("3. Kolika je srednja potrošnja automobila sa 6 cilindara?")
print(round(srednja_potrosnja_6_cil, 2))
print()

srednja_potrosnja_4_cil_masa = mtcars[(mtcars['cyl'] == 4) & (mtcars['wt'] >= 2000) & (mtcars['wt'] <= 2200)]['mpg'].mean()
print("4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?")
print(round(srednja_potrosnja_4_cil_masa, 2))
print()

broj_rucnih_mjenjaca = mtcars[mtcars['am'] == 1]['am'].count()
broj_automatskih_mjenjaca = mtcars[mtcars['am'] == 0]['am'].count()
print("5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?")
print("Ručni mjenjač:", broj_rucnih_mjenjaca)
print("Automatski mjenjač:", broj_automatskih_mjenjaca)
print()

broj_automatskih_snaga_100 = mtcars[(mtcars['am'] == 0) & (mtcars['hp'] > 100)]['am'].count()
print("6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?")
print(broj_automatskih_snaga_100)
print()

print("7. Masa svakog automobila u kilogramima:")
print(mtcars[['car', 'mass_kg']])
