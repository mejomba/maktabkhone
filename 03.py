from collections import Counter
"""
در یک نظرسنجی از افراد علاقه‌­مند به تماشای فیلم، درخواست شد تا 3 تا از ژانرهای مورد علاقه‌­ی خود را بنویسند.
 6 ژانر مختلف برای انتخاب به آن­‌ها داده شده است که شامل:

Horror, Romance, Comedy, History , Adventure , Action

برنامه‎ای بنویسید که تعداد افراد را بگیرد
سپس اسم هر فرد را با ژانرهای مورد علاقش بگیرد
و اسم هر ژانر و تعداد افراد علاقه‌مند به آن ژانر را به ترتیب از بیشترین علاقه‌مندی در خروجی چاپ کند.
( در صورتی که میزان علاقه‌مندی در ژانرهای مختلف یکسان شد، به ترتیب الفبای انگلیسی در خروجی چاپ کنید.)
در صورتی که ژانری انتخاب نشد، مقدار آن را صفر در نظر بگیرید و در خروجی اسم و عدد 0 را چاپ کنید.
"""

number_of_person = int(input())
person_like = []
for like in range(number_of_person):
    person_like_this_genre = input()
    person_like.append(person_like_this_genre.split(' '))

only_genre = []
for i in person_like:
    for j in range(1, 4):
        only_genre.append(i[j])

only_genre.sort()
genre_dice = Counter(only_genre).most_common()
print(genre_dice)
for chap in genre_dice:
    print(f'{chap[0]} : {chap[1]}')

