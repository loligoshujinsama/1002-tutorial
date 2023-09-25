def add(x,y):
    a = x+y
    return a

def subtraction(x,y):
    return x-y

def evenNum(x):
    e=[]
    for i in x:
        if i%2==0:
            e.append(i)
    return len(e)

def maximum(x):
    count = 0
    for i in x:
        if i > count:
            count = i
    return count

def minimum(x):
    count = x[0]
    for i in x:
        if i < count:
            count = i
    return count

def absolute(x):
    x = abs(x)
    return x

def sumTotal(x):
    sum = 0
    for i in x:
        sum += i
    return sum

def clear(x):
    if minimum(x)<5:
        for i in range(len(x)):
            x[i] = 0
    return x

