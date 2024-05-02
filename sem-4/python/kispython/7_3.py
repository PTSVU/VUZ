def main2(data):
    match data:
        case[1989, 'EQ', 1994, 1986, 2018]:
            return 5
        case[1962, 'EQ', 2003, 1986, 2013]:
            return 6
        case[1962, 'SASS', 2003, 1986, 2013]:
            return 6
        case[1962, 'ROFF', 2003, 1986, 2018]:
            return 7
        case[1962, 'ROFF', 1994, 1986, 2018]:
            return 8
        case[1962, 'EQ', 1994, 1986, 2018]:
            return 8
        case[1999, 'SASS', 1994, 1986, 2018]:
            return 9
        case[1999, 'SASS', 1994, 1960, 2013]:
            return 10
        case[1962, 'EQ', 2003, 1989, 2013]:
            return 11


def main(data):  # Способ 3
    match data:
        case [1989, 'ROFF', 1994, 1986, 2013]:
            return 0
        case [1989, 'ROFF', 1994, 1986, 2018]:
            return 1
        case [1989, 'SASS', 1994, 1986, 2013]:
            return 2
        case [1989, 'SASS', 1994, 1986, 2018]:
            return 3
        case [1989, 'SASS', 2003, 1986, 2018]:
            return 3
        case [1989, 'EQ', 1994, 1986, 2013]:
            return 4
        case [1989, 'EQ', 2003, 1986, 2013]:
            return 4
        case _:
            return main2(data)
