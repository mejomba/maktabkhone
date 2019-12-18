import random

list_bazicon = ['حسین' ,' مازیار' ,' اکبر',' نیما'  ,' مهدی' ,' فرهاد' ,' محمد' ,' خشایار',  'میلاد'  ,'مصطفی' , 'امین',' سعید' ,' پویا', 'پوریا' , 'رضا'  ,'علی' , 'بهزاد'  ,'سهیل' ,'بهروز'  ,'شهروز' , 'سامان' , 'محسن',
]
teams = ['A','A','A','A','A','A','A','A','A','A','A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']


def random_name():
    N = random.choice(list_bazicon)
    list_bazicon.remove(N)
    return N


def random_team():
    T = random.choice(teams)
    teams.remove(T)
    return T


"""my approach"""
'''for i in range(11):
    print(random_name(), random_team())'''

class Ensan(object):
    def __init__(self, name=None):
        self.name = name


class Fotbalist(Ensan):
    def __init__(self, name=None, team=None):
        super().__init__(name)
        self.team = team

    def info(self):
        print(f'{self.name} {self.team}')


f1 = Fotbalist(random_name(), random_team()); f2 = Fotbalist(random_name(), random_team())
f3 = Fotbalist(random_name(), random_team()); f4 = Fotbalist(random_name(), random_team())
f5 = Fotbalist(random_name(), random_team()); f6 = Fotbalist(random_name(), random_team())
f7 = Fotbalist(random_name(), random_team()); f8 = Fotbalist(random_name(), random_team())
f9 = Fotbalist(random_name(), random_team()); f10 = Fotbalist(random_name(), random_team())
f11 = Fotbalist(random_name(), random_team()); f12 = Fotbalist(random_name(), random_team())
f13 = Fotbalist(random_name(), random_team()); f14 = Fotbalist(random_name(), random_team())
f15 = Fotbalist(random_name(), random_team()); f16 = Fotbalist(random_name(), random_team())
f17 = Fotbalist(random_name(), random_team()); f18 = Fotbalist(random_name(), random_team())
f19 = Fotbalist(random_name(), random_team()); f20 = Fotbalist(random_name(), random_team())
f21 = Fotbalist(random_name(), random_team()); f22 = Fotbalist(random_name(), random_team())

print("اصلا نتونستم خودمو متقاعد کنم که این پروژه نیاز به شی گرایی داره درواقع\n خیلی کوچیک بود با دوتا لیست و یه حلقه جوابش بدست میومد")
f1.info()
f2.info()
f3.info()
f4.info()
f5.info()
f6.info()
f7.info()
f8.info()
f9.info()
f10.info()
f11.info()
f12.info()
f13.info()
f14.info()
f15.info()
f16.info()
f17.info()
f18.info()
f19.info()
f20.info()
f21.info()
f22.info()
