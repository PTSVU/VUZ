result = []


class MealyMachine:
    def __init__(self):
        self.state = 'A'
        self.transitions = {
            'look': {
                'A': ('E', 2),
                'B': ('C', 3),
                'E': ('G', 7),
                'F': ('G', 8)
            },
            'trim': {
                'A': ('B', 0),
                'D': ('E', 5),
                'E': ('F', 6),
                'G': ('H', 10),
                'H': ('A', 11)
            },
            'speed': {
                'A': ('D', 1),
                'C': ('D', 4),
                'F': ('C', 9)
            }
        }
        global result

    def look(self):
        return self.transition('look')

    def trim(self):
        return self.transition('trim')

    def speed(self):
        return self.transition('speed')

    def transition(self, action):
        if self.state in self.transitions[action]:
            self.state, res = self.transitions[action][self.state]
            result.append(res)
            return res
        else:
            raise MealyError(action)


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
