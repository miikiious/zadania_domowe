import math
a=float(input("podaj pierwszy bok trójkąta: "))
b=float(input("podaj drugi bok trójkąta: "))
c=float(input("podaj trzeci bok trójkąta: "))

trojkat = [a,b,c]
obwod=sum(trojkat)
dłuzszy=max(trojkat)
pobwod=obwod/2
if obwod-dłuzszy<dłuzszy:
    print("trójkąt się nie domyka")
else:
    pole= math.sqrt(pobwod*(pobwod-a)*(pobwod-b)*(pobwod-c))
    print(f'pole trójkąta o takich bokach wynosi {pole}')