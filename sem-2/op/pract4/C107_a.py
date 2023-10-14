import traceback


class Discipline:
    def __init__(self, name, sem, kaf):
        self.name = str(name)
        self.sem = int(sem)
        self.kaf = str(kaf)


try:
    cl = Discipline("name", 1, "kaf")
    assert cl.name == "name"
    assert cl.sem == 1
    assert cl.kaf == "kaf"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()