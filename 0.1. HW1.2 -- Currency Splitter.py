def make_change(coin):
    if coin == 0:
        return {}
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    new_list = {}

    for d in denominations:

        if coin >= d:
            new_list[d] = coin // d
            coin = coin % d

    for key, val in new_list.items():
        print(f"{key} : {val}")

    return new_list


coin = 66
make_change(coin)
