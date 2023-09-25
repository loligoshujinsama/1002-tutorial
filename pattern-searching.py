#!usr/bin/env/python
import sys

def pattern(x,y):
        #Slicing and compare
        c = 0
        for i in range(len(x)-len(y)+1):
            #if i=0, 0:2 equals y (1 2)
            #if i=1, 1:3 equals y (2,3)
            #if i=2, 2:4 (3,1)
            if x[i:i+len(y)] == y:
                c += 1
        return c

if __name__ == "__main__":
    try:
        x = sys.argv[1]
        x = x.split(',')
        y = sys.argv[2]
        y = y.split(',')
        print("Pattern appears %d time!" % (pattern(x,y)))




    except Exception as e:
        print(e.args)
