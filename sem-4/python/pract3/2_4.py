pairs = "..LEXEGEZACEBISOUSESARMAINDIREA.ERATENBERALAVETIEDORQUANTEISRION"

class PlanSys:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.economy = 0
        self.govtype = 0
        self.techlev = 0
        self.population = 0
        self.productivity = 0
        self.radius = 0
        self.goatsoupseed = [0, 0, 0, 0]
        self.name = ""

def tweakseed(s):
    temp = s[0] + s[1] + s[2]
    s[0] = s[1]
    s[1] = s[2]
    s[2] = temp & 0xFFFF

def makesystem(s):
    thissys = PlanSys()
    pair1, pair2, pair3, pair4 = 0, 0, 0, 0
    longnameflag = s[0] & 64

    thissys.x = s[1] >> 8
    thissys.y = s[0] >> 8

    thissys.govtype = (s[1] >> 3) & 7

    thissys.economy = (s[0] >> 8) & 7
    if thissys.govtype <= 1:
        thissys.economy |= 2

    thissys.techlev = (s[1] >> 8) & 3 + (thissys.economy ^ 7)
    thissys.techlev += thissys.govtype >> 1
    if thissys.govtype & 1 == 1:
        thissys.techlev += 1

    thissys.population = 4 * thissys.techlev + thissys.economy
    thissys.population += thissys.govtype + 1

    thissys.productivity = ((thissys.economy ^ 7) + 3) * (thissys.govtype + 4)
    thissys.productivity *= thissys.population * 8

    thissys.radius = 256 * (((s[2] >> 8) & 15) + 11) + thissys.x

    thissys.goatsoupseed = [s[1] & 0xFF, s[1] >> 8, s[2] & 0xFF, s[2] >> 8]

    pair1 = 2 * ((s[2] >> 8) & 31)
    tweakseed(s)
    pair2 = 2 * ((s[2] >> 8) & 31)
    tweakseed(s)
    pair3 = 2 * ((s[2] >> 8) & 31)
    tweakseed(s)
    pair4 = 2 * ((s[2] >> 8) & 31)
    tweakseed(s)

    thissys.name = pairs[pair1:pair1+2] + pairs[pair2:pair2+2] + pairs[pair3:pair3+2]
    name_length = random.randint(3, 6)  # Случайная длина названия от 3 до 6 символов
    thissys.name = ''.join(random.choices(pairs, k=name_length))

    if longnameflag:
        name_length = random.randint(7, 10)  # Случайная длина для длинных названий
        thissys.name += ''.join(random.choices(pairs, k=name_length))

    return thissys


import matplotlib.pyplot as plt

def visualize_galaxy(systems):
    plt.figure(figsize=(10, 6))
    plt.title('Galaxy Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

    for sys in systems:
        plt.scatter(sys.x, sys.y, marker='o', color='black')
        plt.text(sys.x, sys.y, sys.name, fontsize=8, ha='center', va='bottom')

    plt.grid(True)
    plt.tight_layout()
    plt.show()


import random

systems_data = [[random.randint(0, 65535), random.randint(0, 65535), random.randint(0, 65535)] for _ in range(256)]

systems = [makesystem(system_data) for system_data in systems_data]
visualize_galaxy(systems)
