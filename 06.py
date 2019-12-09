"""
4
man I je ich
kheili very très sehr
alaghemand interested intéressé interessiert
barnamenevisi programming laprogrammation Programmierung
I am very interested in programming
"""
"""
man am kheili alaghemand in barnamenevisi
"""
vorodi = int(input())
looping = vorodi + 1
list_jomles = []
for i in range(looping):
    jomles = input()
    list_jomles.append(jomles.split(' '))
for_translate = list_jomles.pop(4)
bias = -1
for translate in for_translate:
    bias += 1
    for list_translate in list_jomles:
        if translate in list_translate:
            for_translate.remove(translate)
            for_translate.insert(bias, list_translate[0])
            break

s = ''
for javab in for_translate:
    s += javab + ' '
print(s.strip(' '))