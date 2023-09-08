#!usr/bin/env/python
import sys

a= sys.argv[1]
b= sys.argv[2]
c= sys.argv[3]
avg=0

#Validate if input is a number
if a.isdigit() and b.isdigit() and c.isdigit():
    avg+=(float(a) + float(b) + float(c))/3

    #Format such that variable avg has 2 decimal points
    print(f"Average:{avg:.2f}")
else:
    print("Your input is invalid!")

