def is_ipv4(address):
    list_adress = address.split('.')
    for l in list_adress:
        if not l.isdigit():
            return False

    if len(list_adress) != 4:
        return False

    for a in list_adress:
      if (int(a) < 0 or int(a) > 255):
            return False

    if list_adress[0][0] == '0' and len(list_adress[0]) > 1:
            return False
    else:
        return True
print(is_ipv4("0.2.2.2"))
