def suma(lista: list) -> int:
    wynik = 0
    for element in lista:
        wynik = wynik + element
    return wynik


def srednia(lista: list) -> float:
    wynik = 0
    for element in lista:
        wynik = wynik + element
    wynik = wynik / len(lista)
    return wynik


def max(lista: list) -> int:
    wynik = lista[0]
    for element in lista:
        if element > wynik:
            wynik = element
    return wynik


def max_minus_min(lista: list) -> int:
    max = lista[0]
    for element in lista:
        if element > max:
            max = element
    min = lista[0]
    for element in lista:
        if element < min:
            min = element
    return max - min


def wypisz_wieksze(lista: list, liczba: float):
    for element in lista:
        if element > liczba:
            print(element)


lista_liczb = [10, 20, 30, 40]
# print(suma(lista_liczb))
# print(srednia(lista_liczb))
# print(max(lista_liczb))
# print(max_minus_min(lista_liczb))
print(wypisz_wieksze(lista_liczb, 20))
