#!usr/bin/env/python

#note: 40 working hours in a week. 
#24hours per day: maximum hours (incl. weekends) = 24*7 = 168hrs/week

import sys

def paym(hours, nrate, orate):
    #payment = normal rate * hours
    if hours>168:
        return "Your input is invalid!"
    elif hours>40:
        hours-=40
        c=(40*nrate)
        b=(hours*orate)
        a=c+b
        return f"Normal Salary:{c:.2f}, Extra Salary:{b:.2f}, Total Salary:{a:.2f}"

    else:
        a=hours*nrate
        b=0
        return f"Normal Salary:{a:.2f}, Extra Salary:{b:.2f}, Total Salary:{a:.2f}"

def valid(a):
    try:
        if float(a) or a.isdigit():
            return True
    except ValueError:
        return False


if len(sys.argv) == 4:
    a1=sys.argv[1]
    a2=sys.argv[2]
    a3=sys.argv[3]
    if valid(a1) and valid(a2) and valid(a3):
        a1=float(a1)
        a2=float(a2)
        a3=float(a3)
        print(paym(a1, a2, a3))
    else:
        print("Your input is invalid!")

else:
    print("Your input is invalid!")
