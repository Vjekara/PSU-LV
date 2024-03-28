
num = []
while True:
    unos = input("unesi broj ili 'Done' za kraj: ")
    if unos == "Done":
        break
    try:
        broj = float(unos)
        num.append(broj)
    except ValueError:
        print("nisi unio broj")
#koliko brojeva, srednju, min i maks vrijednost te sortiraj
if num:
    print(f"ukupno brojeva: {len(num)}")
    print(f"sr vrj brojeva: {sum(num) / len(num)}")
    print(f"min vrj brojeva: {min(num)}")
    print(f"max vrj brojeva: {max(num)}")

    num.sort()
    print(num)
else:
    print("nije unesen broj")