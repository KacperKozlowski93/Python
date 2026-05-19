import random

while True:
    ile_liczb_w_loteri = int(input("Podaj ile liczb ma być losowanych:  "))
    if ile_liczb_w_loteri <= 0:
        print("Podaj przynajmniej 1 liczbę")
        continue
    max_wartosc_liczby = int(input("Podaj max wartosc liczby: "))
    if max_wartosc_liczby < ile_liczb_w_loteri:
        print("Losowanie niemożliwe")
        continue

    lista_losowanych_liczb = random.sample(range(0, max_wartosc_liczby), ile_liczb_w_loteri)

    print(lista_losowanych_liczb)
    print("Sortowanie listy rosnąco: ")
    lista_losowanych_liczb.sort()
    print(lista_losowanych_liczb)
    wyjscie_z_programu = input("Czy losować ponownie? Tak / Nie ")
    if wyjscie_z_programu != "Tak":
        break
