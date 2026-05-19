def to_roman(num):
    lookup_table = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]
    res = ''
    for (n, roman) in lookup_table:
        (d, num) = divmod(num, n)
        res += roman * d
    print(res)


to_roman(1)
to_roman(4)
to_roman(9)
to_roman(40)
to_roman(94)
to_roman(1994)
to_roman(3999)
