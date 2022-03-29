import random
liczb_a=random.randint(0,99)
liczb_b=random.randint(0,99)
suma=int(input(f"podaj sumę {liczb_a}+{liczb_b}= "))
while suma != liczb_a+liczb_b:
    print(f"postaraj się lepiej {liczb_a}+{liczb_b}!={suma}")
    suma = int(input(f"spróbuj jeszcze raz: "))
print("zgadłeś!")