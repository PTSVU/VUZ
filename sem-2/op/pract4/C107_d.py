from C107_b import *
from C107_c import Practice


class Plan:
    def __init__(self, kod_nap, name_nap, kaf, os_dis, practs):
        self.kod_nap = str(kod_nap)
        self.name_nap = str(name_nap)
        self.kaf = str(kaf)
        self.os_dis = os_dis
        self.practs = practs

    def __str__(self):
        print(self.kod_nap, self.name_nap, self.kaf)
        return self.kod_nap, self.name_nap, self.kaf, [self.os_dis[i].__str__() for i in
                                                       range(len(self.os_dis))], self.practs.__str__()

    def __len__(self):
        return len(self.os_dis)

    def __getitem__(self, index):
        try:
            return self.os_dis[index]
        except:
            print("ERROR")

    def __setitem__(self, index, value):
        self.os_dis[index] = value

    def __delitem__(self, index):
        try:
            del self.os_dis[index]
        except:
            print("ERROR")

    def __add__(self, other):
        self.os_dis.append(other)

    def __sub__(self, other):
        try:
            self.os_dis.remove(other)
        except:
            print("ERROR")

    def create_txt(self):
        with open("C107_d.txt", 'w') as f:
            f.write(str(cl.__str__()))
            for os_dis in self.os_dis:
                f.write(f"\nКоличество занятий для {os_dis.name}:\n")
                for les_type, hours in os_dis.hours.items():
                    f.write(f"{les_type}: {hours}\n")
            f.write("\n")


try:
    os_dis = [Academic("name", 1, "kaf", "prepod", "ekz", 1, 2, 3)]
    practs = Practice("name", 1, "kaf", "v_pract", "ruk_pract", "tem_pract")
    cl = Plan("kod_nap", "name_nap", "kaf", os_dis, practs)
    assert cl.kod_nap == "kod_nap"
    assert cl.name_nap == "name_nap"
    assert cl.kaf == "kaf"
    assert len(cl.os_dis) == 1
    assert cl.__len__() == 1
    cl.create_txt()
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
