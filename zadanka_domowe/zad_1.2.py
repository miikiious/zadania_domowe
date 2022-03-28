dni = {1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela'}
print(dni)
dzien = int(input("podaj numer dnia w którym oddano buty: "))
czas = int(input("podaj czas naprawy w dniach: "))
termin = dzien + czas - ((dzien + czas) // 7) * 7
print(f"buty będą gotowe w dzien: {dni.get(termin)}")
