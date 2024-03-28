def ucitaj_i_prebroji_rijeci(ime_datoteke):
    try:
        with open(ime_datoteke, 'r', encoding='utf-8') as datoteka:
            brojac_rijeci = {}
            for line in datoteka:
                rijeci = line.strip().split()
                for rijec in rijeci:
                    rijec = rijec.strip(',').lower()
                    if rijec:
                        if rijec in brojac_rijeci:
                            brojac_rijeci[rijec] += 1
                        else:
                            brojac_rijeci[rijec] = 1
            return brojac_rijeci
    except FileNotFoundError:
        print(f"datoteka '{ime_datoteke}' nije pronadena")
        return None

def ispisi_rijeci_samo_jednom(brojac_rijeci):
    rijeci_samo_jednom = [rijec for rijec, broj in brojac_rijeci.items() if broj == 1]
    print(f"broj rijeci koje se pojavljuju jednom: {len(rijeci_samo_jednom)}")
    print("ove rijecu su:")
    for rijec in rijeci_samo_jednom:
        print(rijec)


ime_datoteke = 'song.txt'
brojac_rijeci = ucitaj_i_prebroji_rijeci(ime_datoteke)
if brojac_rijeci is not None:
    ispisi_rijeci_samo_jednom(brojac_rijeci)