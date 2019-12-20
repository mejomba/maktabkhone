import csv
from sklearn import tree, preprocessing
car_name = []
unique_car = []
x = []
y = []
with open('final_car.csv', 'r', encoding='utf-8') as d:
    data = csv.reader(d)
    for line in data:
        car_name.append(line[0])
        x.append(line[0:3])
        y.append(line[3])

for unique in car_name:
    if unique not in unique_car:
        unique_car.append(unique)
for car in enumerate(unique_car, 1):
    print(f"{car[1]} <== {car[0]}")


print('******************')
print("فارسی و انگلیسی خیلی خوب کنار هم قرار نمیگیرن...")
your_car = int(input("Select You'r Car= (یک عدد از 1 تا 15)"))
print(f'you select {unique_car[your_car-1]}')
your_work = int(input("میزان کارکرد (کیلومتر)= "))
your_age = int(input("عمر خودرو= "))

your_data = [[unique_car[your_car-1], your_work, your_age]]

n_car_encode = []
car_encode = []
le = preprocessing.LabelEncoder()
le.fit_transform(unique_car)
transform = le.transform(unique_car)
n_car_encode.append(transform)

for e in n_car_encode[0]:
    car_encode.append(e)

car_dic = dict(zip(unique_car, car_encode))

for i in range(len(x)):
    x[i][0] = car_dic.get(x[i][0])

your_data[0][0] = car_dic[your_data[0][0]]

clf = tree.DecisionTreeClassifier()
clf.fit(x,y)
ans = clf.predict(your_data)

print(f"yor car, with {your_work}km work & {your_age} year's age >>> price= {ans[0]} ")
