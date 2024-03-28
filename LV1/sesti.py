def izracunaj_statistiku(file):
    broj_ham_poruka = 0
    broj_spam_poruka = 0
    ukupno_rijeci_ham = 0
    ukupno_rijeci_spam = 0
    spam_zavrsava_usklicnikom = 0

    with open(file, 'r', encoding='utf-8') as f:
        for linija in f:
            tip, poruka = linija.split('\t', 1)
            broj_rijeci = len(poruka.split())

            if tip == 'ham':
                broj_ham_poruka += 1
                ukupno_rijeci_ham += broj_rijeci
            elif tip == 'spam':
                broj_spam_poruka += 1
                ukupno_rijeci_spam += broj_rijeci
                if poruka.strip().endswith('!'):
                    spam_zavrsava_usklicnikom += 1

    prosjek_rijeci_ham = ukupno_rijeci_ham / broj_ham_poruka if broj_ham_poruka > 0 else 0
    prosjek_rijeci_spam = ukupno_rijeci_spam / broj_spam_poruka if broj_spam_poruka > 0 else 0

    return prosjek_rijeci_ham, prosjek_rijeci_spam, spam_zavrsava_usklicnikom

datoteka = 'SMSSpamCollection.txt'
prosjek_ham, prosjek_spam, broj_spam_usklicnik = izracunaj_statistiku(datoteka)

print(f"Prosjek riječi u ham porukama: {prosjek_ham:.2f}")
print(f"Prosjek riječi u spam porukama: {prosjek_spam:.2f}")
print(f"Broj spam poruka koje završavaju uskličnikom: {broj_spam_usklicnik}")