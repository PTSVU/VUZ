def main(data: list) -> int:  # Способ 1
    if data[3] == 1989:
        return 11
    elif data[3] == 1960:
        return 10
    elif data[3] == 1986:
        return data0(data)


def data0(data: list) -> int:
    if data[0] == 1999:
        return 9
    elif data[0] == 1962:
        return data2(data)
    elif data[0] == 1989:
        if data[1] == "EQ":
            return data_eq(data)
        elif data[1] == "SASS":
            return data_sass(data)
        elif data[1] == "ROFF":
            return data_roff(data)


def data2(data: list) -> int:
    if data[2] == 1994:
        return 8
    elif data[2] == 2003:
        if data[4] == 2018:
            return 7
        elif data[4] == 2013:
            return 6


def data_eq(data: list) -> int:
    if data[4] == 2018:
        return 5
    elif data[4] == 2013:
        return 4


def data_sass(data: list) -> int:
    if data[4] == 2018:
        return 3
    elif data[4] == 2013:
        return 2


def data_roff(data: list) -> int:
    if data[4] == 2018:
        return 1
    elif data[4] == 2013:
        return 0
