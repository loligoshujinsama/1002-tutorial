#!usr/bin/env/python
import sys


if __name__ == "__main__":
    try:
        year1=int(sys.argv[1])
        year2=int(sys.argv[2])
        check1=[]
        for i in range(year1, year2+1):
            if i%4 == 0:
                check1.append(i)
            else:
                pass

        for i in check1:
            if i%100 == 0 and i%400 != 0:
                check1.remove(i)
            else:
                pass
            
        output=""
        for i in range(len(check1)):
            if i==(len(check1)-1):
                output+=str(check1[i])
            else:
                output+=str(check1[i])+", "

        print(f"The number of Leap Years is {len(check1)}, the Leap Years are {output}")
    except Exception as e:
        print("Your input is invalid!") 
