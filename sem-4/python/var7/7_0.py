def main(data: list) -> int:
    if data[3] == 1989:
        return 11
    elif data[3] == 1960:
        return 10
    elif data[3] == 1986:
        if data[0] == 1999:
            return 9
        elif data[0] == 1962:
            if data[2] == 1994:
                return 8
            elif data[2] == 2003:
                if data[4] == 2018:
                    return 7
                elif data[4] == 2013:
                    return 6
        elif data[0] == 1989:
            if data[1] == "EQ":
                if data[4] == 2018:
                    return 5
                elif data[4] == 2013:
                    return 4
            elif data[1] == "SASS":
                if data[4] == 2018:
                    return 3
                elif data[4] == 2013:
                    return 2
            elif data[1] == "ROFF":
                if data[4] == 2018:
                    return 1
                elif data[4] == 2013:
                    return 0


print(main([1962, 'EQ', 2003, 1989, 2013]))  # 11
print(main([1989, 'SASS', 1994, 1986, 2013]))  # 2
print(main([1999, 'SASS', 1994, 1960, 2013]))  # 10
print(main([1999, 'SASS', 1994, 1986, 2018]))  # 9
print(main([1962, 'ROFF', 2003, 1986, 2018]))  # 7

print()

print(main([1989, 'ROFF', 1994, 1986, 2013]))  # 0
print(main([1989, 'ROFF', 1994, 1986, 2018]))  # 1
print(main([1989, 'SASS', 1994, 1986, 2013]))  # 2
print(main([1989, 'SASS', 1994, 1986, 2018]))  # 3
print(main([1989, 'EQ', 1994, 1986, 2013]))  # 4
print(main([1989, 'EQ', 1994, 1986, 2018]))  # 5
print(main([1962, 'EQ', 2003, 1986, 2013]))  # 6
print(main([1962, 'ROFF', 2003, 1986, 2018]))  # 7
print(main([1962, 'ROFF', 1994, 1986, 2018]))  # 8
print(main([1999, 'SASS', 1994, 1986, 2018]))  # 9
print(main([1999, 'SASS', 1994, 1960, 2013]))  # 10
print(main([1962, 'EQ', 2003, 1989, 2013]))  # 11

print()

print(main([1962, 'SASS', 2003, 1986, 2013]))