class School(object):
    def __init__(self, tedad, sen, ghad, vazn):
        self.tedad = tedad
        self.sen = sen
        self.ghad = ghad
        self.vazn = vazn

    def __sen_mid(self):
        self.mid_sen = sum(self.sen) / self.tedad[0]
        return self.mid_sen

    def __ghad_mid(self):
        self.mid_ghad = sum(self.ghad) / self.tedad[0]
        return self.mid_ghad

    def __vazn_mid(self):
        self.mid_vazn = sum(self.vazn) / self.tedad[0]
        return self.mid_vazn

    def info(self):
        print(self.__sen_mid())
        print(self.__ghad_mid())
        print(self.__vazn_mid())
        if a.__ghad_mid() > b.__ghad_mid():
            print('A')
        elif a.__ghad_mid() < b.__ghad_mid():
            print('B')
        elif a.__ghad_mid() == b.__ghad_mid() and a.__vazn_mid() < b.__vazn_mid():
            print('A')
        elif a.__ghad_mid() == b.__ghad_mid() and a.__vazn_mid() > b.__vazn_mid():
            print('B')
        else:
            print('Same')

sen_a = []
ghad_a = []
vazn_a = []
sen_b = []
ghad_b = []
vazn_b = []
tedad_a = []
tedad_b = []

for i in range(8):
    x = input()
    if i == 0:
        tedad_a.append(int(x))
    elif i == 1:
        sen = x.split(' ')
        for a in sen:
            sen_a.append(int(a))
    elif i == 2:
        ghad = x.split(' ')
        for a in ghad:
            ghad_a.append(int(a))
    elif i == 3:
        vazn = x.split(' ')
        for a in vazn:
            vazn_a.append(int(a))
    elif i == 4:
        tedad_b.append(int(x))
    elif i == 5:
        sen = x.split(' ')
        for a in sen:
            sen_b.append(int(a))
    elif i == 6:
        ghad = x.split(' ')
        for a in ghad:
            ghad_b.append(int(a))
    elif i == 7:
        vazn = x.split(' ')
        for a in vazn:
            vazn_b.append(int(a))

a = School(tedad_a, sen_a, ghad_a, vazn_a)
b = School(tedad_b, sen_b, ghad_b, vazn_b)

a.info()
b.info()
