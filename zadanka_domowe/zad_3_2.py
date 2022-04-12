def ile_dni_miesiac(miesiac: str, rok: int = 1) -> int:
    lista_a = ["styczen", "marzec", "maj", "lipiec", "sierpien", "pazdziernik", "grudzien"]
    lista_b = ["kwiecen", "czerwiec", "wrzesien", "listopad"]
    if miesiac in lista_a:
        dni = 31
    elif miesiac in lista_b:
        dni = 30
    else:
        if rok % 4 == 0:
            dni = 29
        else:
            dni = 28
    return dni


rok = 1
miesiac = input("podaj miesiąc: ")
if miesiac == "luty":
    rok = int(input("podaj rok: "))
dni = ile_dni_miesiac(miesiac, rok)
print(f"miesiąc {miesiac} ma {ile_dni_miesiac(miesiac, rok)}")
