#!usr/bin/env/python

import sys

def valid(a):
    try:
        if float(a) or a.isdigit():
            return True
    except ValueError:
        return False

def table(b):
    if b<16:
        return "Severe Thinness"
    elif 16<=b<=17:
        return "Moderate Thinness"
    elif 17<=b<=18.5:
        return "Mild Thinness"
    elif 18.5<=b<=25:
        return "Normal"
    elif 25<=b<=30:
        return "Overweight"
    elif 30<=b<=35:
        return "Obese Class I"
    elif 35<=b<=40:
        return "Obese Class II"
    elif b>40:
        return "Obese Class III"
    else:
        return "Error"


if len(sys.argv) == 4:
    a = sys.argv[1]
    h = sys.argv[2] #height
    w = sys.argv[3] #weight
    bmi=0

    if a.lower() == "metric":
        if valid(h) and valid(w) is True:
            h=float(h)
            w=float(w)
            bmi=(w/(h**2))
            print(("%0.2f\t"%bmi)+table(bmi))
        else:
            print("Your input is invalid!")

    elif a.lower() == "imperial":
        if valid(h) and valid(w) is True:
            w=float(w)
            h=float(h)
            bmi=((703*w)/h**2)
            print(("%0.2f\t"%bmi)+table(bmi))
    else:
        print("Your input is invalid!")

else:
    print("Your input is invalid!")






