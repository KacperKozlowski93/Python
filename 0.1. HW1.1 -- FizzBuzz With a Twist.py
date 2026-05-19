n = int(input("Podaj liczbę: "))
wynik = ""
if n % 3 == 0:
    wynik += "Fizz"
if n % 5 == 0:
    wynik += "Buzz"
if n % 7 == 0:
    wynik += "Bang"
if (n % 3 != 0) and (n % 5 != 0) and (n % 7 != 0):
    wynik = n

print(wynik)


