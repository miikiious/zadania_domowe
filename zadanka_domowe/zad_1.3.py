waga=float(input("podaj wagę w kg: "))
wzrost=float(input("podaj wzrost w m: "))
bmi=waga/(wzrost**2)
print(f"BMI wynosi: {bmi:.2f}")
if bmi<18.5:
    print("za niskie, pomyśl nad jedzeniem więcej")
elif 18.5<=bmi<=24.99:
    print('optymalne, oby tak dalej')
else:
    print("za wysokie, pomyśl nad schudnięciem")