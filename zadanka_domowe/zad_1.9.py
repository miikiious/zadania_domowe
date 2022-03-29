
for liczba in range(1, 100):
    if liczba % 15 == 0:
        print('FizzBuzz')
    elif liczba % 3 == 0:
        print('Fizz')
    elif liczba % 5 == 0:
        print('Buzz')
    else:
        print(liczba)
