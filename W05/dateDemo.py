import datetime as dt

yesterday = dt.date(2023, 9, 25)
today = dt.date.fromisoformat("2023-09-26")

print(yesterday)
print(today)
print("Yes") if today > yesterday else print("NO")