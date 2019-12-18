'The Persian League is the largest sport event dedicated to the deprived areas of Iran. The Persian League promotes peace and friendship. This video was captured by one of our heroes who wishes peace.'

in_str = input()
list_str = in_str.split('.')

new_list_str = []
for a in list_str:
    new_list_str.append(a.replace(',', ''))

list_str2 = []
list_str3 = []
list_str4 = []
for i in new_list_str:
    list_str2.append(i.strip(" "))
for j in list_str2:
    list_str3.append(j.split(" "))
for f in list_str3:
    for g in range(1, len(f)):
        list_str4.append(f[g])


def x(l):
    none = 0
    bias = 0
    for wl in l:
        for w in range(1, len(wl)):
            if wl[w].istitle():
                print(f'{w + 1 + bias}:{wl[w]}')
                none += 1
        bias += len(wl)
    if none == 0:
        print(None)


x(list_str3)
