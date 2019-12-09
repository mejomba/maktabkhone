"""
4
m.hosSein.python
f.miNa.C
m.aHMad.C++
f.Sara.java
"""

"""
f Mina C
f Sara java
m Ahmad C++
m Hossein python
"""

number_of_user = int(input())
user_list = []
for i in range(number_of_user):
    user = input()
    user_list.append(user.split('.'))
for j in user_list:
    j.insert(1, j[1].lower())
    j.pop(2)
user_list.sort()
for k in user_list:
    print(f'{k[0]} {k[1].capitalize()} {k[2]}')
