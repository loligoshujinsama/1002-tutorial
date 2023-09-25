from myMath import *
import sys

try:
    x = sys.argv[1]
    
    x = x.split(",")
    if len(x) != 1:
        for i in range(len(x)):
            x[i] = int(x[i])
        
        maxNum = maximum(x)
        minNum = minimum(x)
        print("The difference is:%d The summation is:%d The summation of all input is:%d The number of even numbers is:%d The values in the list are: %s" % (subtraction(maxNum, minNum),add(maxNum, minNum), sumTotal(x), evenNum(x), clear(x)))    
    else:
        a = absolute(int(x[0]))
        print(a)



except Exception as e:
    print(e)