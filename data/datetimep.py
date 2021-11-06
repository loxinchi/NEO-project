import datetime

d = datetime.datetime.strptime("1900-Jan-01 02:33", "%Y-%b-%d %H:%M")
print(d)
e = datetime.datetime.strftime(d, "%Y-%m-%d %H:%M")
print(e)

print(e.split())
