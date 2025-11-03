import datetime

today = datetime.date.today()-datetime.timedelta(hours=9)
print(today.year)
print(today.month)
print(today.day)