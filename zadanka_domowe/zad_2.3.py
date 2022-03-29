liczba = float(input("Podaj liczbę: "))
suma = liczba
ilosc = 1
min = liczba
max = liczba
while liczba != "y":
    liczba = input("Podaj liczbę, a jeśli skończyłeś podaj [y]: ")
    if liczba != "y":
        liczba = float(liczba)
        suma = suma + liczba
        ilosc += 1
        srednia = suma / ilosc
        if min > liczba:
            min = liczba
        if max < liczba:
            max = liczba
print(f"ilość liczb: {ilosc}\n"
      f"suma: {suma}\n"
      f"średnia: {srednia}\n"
      f"minimum: {min}\n"
      f"maksimum: {max}")
