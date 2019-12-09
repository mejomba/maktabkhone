import random

list_bazicon = ['حسین' ,' مازیار' ,' اکبر',' نیما'  ,' مهدی' ,' فرهاد' ,' محمد' ,' خشایار',  'میلاد'  ,'مصطفی' , 'امین',' سعید' ,' پویا', 'پوریا' , 'رضا'  ,'علی' , 'بهزاد'  ,'سهیل' ,'بهروز'  ,'شهروز' , 'سامان' , 'محسن',
]
team_a = []
team_b = []


class Ensan(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        #self.height = height
        #self.age = age
        #self.weight = weight



class Fotbalist(Ensan):
    pass


hosein = Fotbalist('حسین');maziar = Fotbalist('مازیار');akbar = Fotbalist('اکبر')
nima = Fotbalist('نیما');mahdi = Fotbalist('مهدی');farhad = Fotbalist('فرشاد')
mohamad = Fotbalist('محمد');khashayar = Fotbalist('خشایار');milad = Fotbalist('میلاد')
mostafa = Fotbalist('مصتفا');amin = Fotbalist('امین');said = Fotbalist('سعید')
poya = Fotbalist('پویا');poria = Fotbalist('پوریا');reza = Fotbalist('رضا')
ali = Fotbalist('علی');bahzad = Fotbalist('بهزاد');soheil = Fotbalist('سهیل')
behroz = Fotbalist('بهروز');shahroz = Fotbalist('شهروز');saman = Fotbalist('سامان');mohsen = Fotbalist('محسن')


for i in range(11):
    a = random.choice(list_bazicon)
    team_a.append(a)
    list_bazicon.remove(a)
    b = random.choice(list_bazicon)
    team_b.append(b)
    list_bazicon.remove(b)


for i in team_a:
    print(f"{i} A")
for j in team_b:
    print(f"{j} B")