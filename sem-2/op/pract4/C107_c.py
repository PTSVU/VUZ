from C107_a import *


class Practice(Discipline):
    def __init__(self, name, sem, kaf, v_pract, ruk_pract, tem_pract):
        Discipline.__init__(self, name, sem, kaf)
        self.v_pract = str(v_pract)
        self.ruk_pract = str(ruk_pract)
        self.tem_pract = []
        self.tem_pract.append(str(tem_pract))

    def __str__(self):
        print(self.name, self.sem, self.kaf, self.v_pract, self.ruk_pract, self.tem_pract)
        return self.name, self.sem, self.kaf, self.v_pract, self.ruk_pract, self.tem_pract

    def change_ruk(self, new_ruk):
        self.ruk_pract = new_ruk

    def add_tem(self, new_tem):
        self.tem_pract.append(new_tem)

    def del_tem(self, del_name):
        self.tem_pract.remove(del_name)

    def change_tem(self, old_tem, new_tem):
        for i in range(len(self.tem_pract)):
            if self.tem_pract[i] == old_tem:
                self.tem_pract[i] = new_tem


try:
    cl = Practice("name", 1, "kaf", "v_pract", "ruk_pract", "tem_pract")
    assert cl.name == "name"
    assert cl.sem == 1
    assert cl.kaf == "kaf"
    assert cl.v_pract == "v_pract"
    assert cl.ruk_pract == "ruk_pract"
    cl.change_ruk("new_ruk")
    assert cl.ruk_pract == "new_ruk"
    cl.add_tem("new_tem")
    assert cl.tem_pract[-1] == "new_tem"
    cl.del_tem("new_tem")
    assert ("new_tem" in cl.tem_pract) == False
    cl.change_tem("tem_pract", "new_tem")
    assert ("new_tem" in cl.tem_pract) == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()