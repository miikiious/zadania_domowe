wysokosc = int(input("podaj wysokość choinki: "))
a = 1
while a < wysokosc + 1:
    print(" " * (2*wysokosc - 2*a), " *"*a, "* "*(a-1))
    a += 1
