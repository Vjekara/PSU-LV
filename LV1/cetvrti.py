def izracunaj_srj_spam_confidence(ime_fajla):
    try:
        with open(ime_fajla, 'r') as file:
            total_confidence = 0
            brojac = 0
            for line in file:
                if line.startswith('X-DSPAM-Confidence: '):

                    confidence = float(line.strip().split(':')[1])
                    total_confidence+=confidence
                    brojac += 1
            if brojac > 0 :
                srj_confidence = total_confidence / brojac
                print("srednja X-DSPAM-Confidence: ", srj_confidence)
            else:
                print("nema 'X-DSPAM-Confidence:' ")
    except FileNotFoundError:
        print("file nije pronadjen")
    except Exception as e:
        print("doslo je do errora:", e)
    finally:
        try:
            file.close()
        except:
            pass

ime_fajla = input("ime datoteke: ")
izracunaj_srj_spam_confidence(ime_fajla)