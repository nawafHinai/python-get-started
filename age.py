from datetime import date
import argparse

def myAge(birthDay):
    today = date.today()
    age = today - birthDay
    return age

parser = argparse.ArgumentParser(description= "abumother it class")

parser.add_argument("year",type= int)
parser.add_argument("month",type= int)
parser.add_argument("day",type= int)
parser.add_argument("age")

args = parser.parse_args()

print(args)