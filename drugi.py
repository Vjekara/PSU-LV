try:
    score = float(input("unesi ocjeni izmedju 0.0 i 1.0: "))

    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("uneseni broj je izvan intervala")
except ValueError:

    print("unos nije broj")