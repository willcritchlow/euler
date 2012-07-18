import datetime

d1 = datetime.date(1901,1,1)
delta5 = datetime.timedelta(days=5)
delta7 = datetime.timedelta(days=7)
first_sunday = d1 + delta5
end = datetime.date(2000, 12, 31)

day = first_sunday
first_of_month = 0
while True:
    day += delta7
    if day > end:
        print first_of_month
        exit()
    if day.day == 1:
        first_of_month += 1
