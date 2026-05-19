while True:
    try:
        temperatura_w_stopniach_celsjusza = float(input("Podaj temperature w stopniach Celsjusza: "))
        temperatura_w_stopniach_fahrenheita = (temperatura_w_stopniach_celsjusza * 9 / 5) + 32
        break
    except ValueError:
        print("Złe dane, spróbuj jeszcze raz")

print(f"Temperatura w stopniach fahrenheita wynosi: {temperatura_w_stopniach_fahrenheita:.1f}")