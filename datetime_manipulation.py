import datetime
from datetime import date

print("minimum representable year is :")
print(datetime.MINYEAR)

print("maximum representable year is :")
print(datetime.MAXYEAR)

print("the represented year is :")
print(datetime.date(1999,7,7))

print("today is :")
print(date.today())

print("the from time stamp is :")
print(date.fromtimestamp(99000))

print("min is :")
print(date.min)

print("max is :")
print(date.max)