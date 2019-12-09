"""
برنامه‌ای بنویسید که 10 عدد از ورودی بخواند
 و در انتها عددی که بیشترین تعداد مقسوم‌علیه عدد اول را دارد به همراه تعداد مقسوم‌علیه‌های اول آن، در خروجی چاپ کند.
 اگر چند عدد این حالت را داشتند، بزرگترین آن‌ها را چاپ کند.
"""
import math
input_list = []
list_maghsom = []
list_maghsom2 = []
list_maghsom_aval = []

def aval(num):
    if num == 1:
        return None
    c = 0
    for adad in range(2, int(math.sqrt(num))+1):
        if num % adad == 0:
            c += 1
    if c == 0 :
        return num


for i in range(10):
    input_list .append(int(input()))

for number in input_list:
    list_maghsom = []
    for x in range(1, number+1):
        if number % x == 0:
            list_maghsom.append(x)
    list_maghsom2.append(number)
    for adad_aval in list_maghsom:
        list_maghsom2.append(aval(adad_aval))
    list_maghsom_aval.append(list_maghsom2)
    list_maghsom2 = []


w = []
q = []
for list1 in list_maghsom_aval:
    list_maghsom_aval = []
    w = (list(filter(lambda a: a != None, list1)))
    q.append(w)

len_tol = []
for tol in q:
    len_tol.append(len(tol))
max_len_tol = max(len_tol)
list_max_element = []
for tol2 in q:
    if len(tol2) == max_len_tol:
        list_max_element.append(tol2[0])
max_big = max(list_max_element)
print(max_big, max_len_tol-1)

