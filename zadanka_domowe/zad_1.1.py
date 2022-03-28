
ziemniaki_cena = float(input("podaj cenę ziemniaków w zł za kg: "))
ziemniaki_ilosc = float(input("podaj ilość ziemniaków w kg: "))
banany_cena = float(input("podaj cenę bananów w zł za kg: "))
banany_ilosc = float(input("podaj ilość bananów w kg: "))
ziemniaki = ziemniaki_cena * ziemniaki_ilosc
banany = banany_cena * banany_ilosc

print(f'do zapłaty masz łącznie {banany+ziemniaki}zł')
if banany > ziemniaki:
    print('banany ciebie drożej kosztowały')
elif ziemniaki > banany:
    print("ziemniaki ciebie drożej kosztowały")
else:
    print("banany i ziemniaki kosztowały dokładnie tyle samo")