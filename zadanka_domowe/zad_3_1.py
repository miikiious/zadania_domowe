def stopy_na_metry(dlugosc: float) -> float:
    dlugosc = dlugosc * 0.3048
    return dlugosc


def max(liczba1: float, liczba2: float) -> float:
    if liczba1 <= liczba2:
        max = liczba2
    else:
        max = liczba1
    return max


def srednia(liczba1: float, liczba2: float) -> float:
    srednia = (liczba1 + liczba2)/2
    return srednia


# szkoda czasu na inne

# stopy = float(input("podaj dlugość w stopach: "))
# print(f"{stopy} stóp to {stopy_na_metry(stopy):.2f} metrów")

# l1 = float(input("podaj pierwszą liczbę: "))
# l2 = float(input("podaj drugą liczbę: "))
# print(f"max z {l1} i {l2} to {max(l1, l2)}")

# l1 = float(input("podaj pierwszą liczbę: "))
# l2 = float(input("podaj drugą liczbę: "))
# print(f"średnia z {l1} i {l2} to {srednia(l1, l2)}")

