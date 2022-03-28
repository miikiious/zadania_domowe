import random

typ = None
strzaly = 0
liczba = random.randint(0, 999)
while typ != liczba:
    typ = int(input("Spróbuj zgadnąć liczbę: "))
    strzaly += 1
    if typ > liczba:
        print("Liczba jest mniejsza od podanej, spróbuj jeszcze raz")
    elif typ < liczba:
        print("Liczba jest większa od podanej, spróbuj jeszcze raz")
else:
    print("Brawo zgadłeś")
    print(f"ilość prób to: {strzaly}")
