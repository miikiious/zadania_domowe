wiek = int(input("podaj wiek: "))
pobyt = int(input("podaj długość pobytu w dniach"))
mnoznik = 1

if wiek < 18:
    mnoznik = 100
elif wiek >= 18:
    if pobyt == 1:
        mnoznik = 200
    elif 1 < pobyt < 5:
        mnoznik = 180
    else:
        mnoznik = 150
if wiek >= 65:
    mnoznik *= 0.9
cena=mnoznik*pobyt
print(f'Do zapłaty za {pobyt} dni należy się {cena}zł')