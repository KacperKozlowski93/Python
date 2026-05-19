while True:
    try:
        a = float(input("Podaj pierwszą liczbę: "))
        operator = input("Podaj operator: + , - , * lub / ")
        if (operator != '+' and operator != '-' and operator != '*' and operator != '/'):
            print("Niepoprawny operator, spróbuj ponownie")
            continue
        b = float(input("Podaj drugą liczbę: "))
        if operator == '+':
            print(a + b)
        elif operator == '-':
            print(a - b)
        elif operator == '*':
            print(a * b)
        elif operator == '/':
            print(a / b)
    except (ZeroDivisionError):
        print("dont crash")
        break
    except:
        print("Nieprawidłowe dane, podaj jeszcze raz")