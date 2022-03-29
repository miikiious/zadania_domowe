wiek = int(input("podaj wiek w latach: "))
ile = int(input("podaj ile biletów chcesz kupić: "))

if 0 <= wiek <= 6:
    cena = 0
elif 17 >= wiek >= 7:
    cena = 2.27
elif 18 <= wiek <= 64:
    cena = 3.80
else:
    cena = 1.90
dozapłaty = ile * cena
print(f'do zapłaty jest {dozapłaty}zł za {ile} biletów')