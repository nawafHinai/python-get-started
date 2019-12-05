from datetime import date

def myAge(birthDay):
    today = date.today()
    age = today.year - birthDay.year
    return age

year = input("year: ")
mon = input("month: ")
day = input("day: ")

age = myAge(date(year,mon,day))

print(age , "years")