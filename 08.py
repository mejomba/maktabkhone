import datetime
current_time = datetime.datetime.today()


born = input()
year, month, day = [int(f) for f in born.split('/')]


if 31 >= day >= 0:
    if 12 >= month >= 0:
        if month > current_time.month or (month == current_time.month and day > current_time.day):
            x = int(current_time.year) - year - 1
            print(x)
        else:
            x = int(current_time.year) - year
            print(x)
    else:
        print("WRONG")
else:
    print("WRONG")
