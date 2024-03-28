def total_euro(sati, satnica):
    return sati*satnica

sati = input('radni sati: ')
satnica = input('eura/h: ')

sati = float(sati)
satnica = float(satnica)

ukupno = total_euro(sati, satnica)
print("Ukupno: ", ukupno)