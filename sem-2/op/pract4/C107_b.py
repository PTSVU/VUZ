from C107_a import *


class Academic(Discipline):
    def __init__(self, name, sem, kaf, prepod, ekz, lek_hours, lab_hours, prakt_hours):
        Discipline.__init__(self, name, sem, kaf)
        self.prepod = str(prepod)
        self.ekz = str(ekz)
        self.hours = {
            "lek": int(lek_hours),
            "lab": int(lab_hours),
            "prakt": int(prakt_hours)
        }

    def __str__(self):
        print(self.name, self.sem, self.kaf, self.prepod, self.ekz)
        return self.name, self.sem, self.kaf, self.prepod, self.ekz

    def change_prepod(self, new_prepod):
        self.prepod = str(new_prepod)

    def change_ekz(self, new_ekz):
        self.ekz = str(new_ekz)

    def print_hours(self):
        print(self.hours)


try:
    cl = Academic("name", 1, "kaf", "prepod", "ekz", 1, 2, 3)
    assert cl.name == "name"
    assert cl.sem == 1
    assert cl.kaf == "kaf"
    assert cl.prepod == "prepod"
    assert cl.ekz == "ekz"
    cl.change_prepod("new_prepod")
    assert cl.prepod == "new_prepod"
    cl.change_ekz("new_ekz")
    assert cl.ekz == "new_ekz"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()