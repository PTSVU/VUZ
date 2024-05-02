result = []


class MealyMachine:
    def __init__(self):
        self.state = 'A'
        global result

    def look(self):
        if self.state == 'A':
            self.state = 'E'
            result.append(2)
            return 2
        elif self.state == 'B':
            self.state = 'C'
            result.append(3)
            return 3
        elif self.state == 'E':
            self.state = 'G'
            result.append(7)
            return 7
        elif self.state == 'F':
            self.state = 'G'
            result.append(8)
            return 8
        else:
            raise MealyError('look')

    def trim(self):
        if self.state == 'A':
            self.state = 'B'
            result.append(0)
            return 0
        elif self.state == 'D':
            self.state = 'E'
            result.append(5)
            return 5
        elif self.state == 'E':
            self.state = 'F'
            result.append(6)
            return 6
        elif self.state == 'G':
            self.state = 'H'
            result.append(10)
            return 10
        elif self.state == 'H':
            self.state = 'A'
            result.append(11)
            return 11
        else:
            raise MealyError('trim')

    def speed(self):
        if self.state == 'A':
            self.state = 'D'
            result.append(1)
            return 1
        elif self.state == 'C':
            self.state = 'D'
            result.append(4)
            return 4
        elif self.state == 'F':
            self.state = 'C'
            result.append(9)
            return 9
        else:
            raise MealyError('speed')


class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name
        global result


def main():
    return MealyMachine()


def test():
    global result
    o = main()
    assert o.look() == 2
    assert o.trim() == 6
    try:
        o.trim()
    except MealyError:
        pass
    assert o.look() == 8
    assert o.trim() == 10
    assert o.trim() == 11
    assert o.speed() == 1
    assert o.trim() == 5
    assert o.trim() == 6
    assert o.speed() == 9
    assert o.speed() == 4
    try:
        o.speed()
    except MealyError:
        pass
    assert o.trim() == 5
    assert o.look() == 7
    try:
        o.look()
    except MealyError:
        pass
    assert o.trim() == 10
    assert o.trim() == 11
    assert o.trim() == 0
    assert o.look() == 3
    o = main()
    assert o.look() == 2
    assert o.look() == 7
    assert o.trim() == 10
    assert o.trim() == 11
    assert o.speed() == 1
    assert o.trim() == 5
    assert o.trim() == 6
    assert o.look() == 8
    assert o.trim() == 10
    assert o.trim() == 11
    assert o.trim() == 0
    assert o.look() == 3
    assert o.speed() == 4
    assert o.trim() == 5
    assert o.trim() == 6
    assert o.speed() == 9
    result = []

    try:
        o = main()
        assert o.look() == 2
        assert o.trim() == 6
        o.trim()
    except MealyError as e:
        pass
    return result
