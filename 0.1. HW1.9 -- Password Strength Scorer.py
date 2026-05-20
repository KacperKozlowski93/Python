


def score(a):
    result = (
            (len(a) >= 8) * 20 +
            (len(a) >= 12) * 10 +
            (len(a) >= 16) * 10 +
            (any(char.isdigit() for char in a)) * 10 +
            (a.islower()) * 10 +
            (a.isupper()) * 10 +
            (not a.isdigit() and not a.isalpha()) * 20
            

    )

    return result


print(score("zaaaaaa!"))
