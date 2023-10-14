import traceback
import re

def NDS(email):
    if re.search(r'@', str(email)) != 0 and re.search(r'.', str(email)) != 0:
        nik = ""
        dom = ""
        suf = ""
        domm = 0
        suff = 0
        for i in range(len(email)):
            if domm == 0 and suff == 0 and email[i] != "@":
                nik += email[i]
            if domm == 1 and suff == 0 and email[i] != "@" and email[i] != ".":
                dom += email[i]
            if domm == 1 and suff == 1 and email[i] != "@" and email[i] != ".":
                suf += email[i]
            if domm == 0 and email[i+1] == "@":
                domm = 1
                i += 1
            if suff == 0 and email[i] == "." and domm == 1:
                suff = 1
                i += 1
        ot = [nik, dom, suf]
        if len(nik) < 3 or len(dom) < 3 or len(suf) < 2:
            return None
        return ot
    else:
        return None


try:
    ot = ['z.uck26', 'facebook', 'com']
    assert NDS("z.uck26@facebook.com") == ot
    ot = ['page33', 'google', 'com']
    assert NDS("page33@google.com") == ot
    ot = ['jeff42', 'amazon', 'com']
    assert NDS("jeff42@amazon.com") == ot
    ot = None
    assert NDS("j@amazon.com") == None
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")