from jalaali import Jalaali
from datetime import date
print(Jalaali.to_jalaali(2019,12,16))

today = str(date.today()).split('-')


today_jalali = Jalaali.to_jalaali(int(today[0]),int(today[1]),int(today[2]))
print(today_jalali['jy'])
print(int(today[0]))

