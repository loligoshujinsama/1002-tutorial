#!usr/bin/env/python
import sys

def letter_count(x):
    db={}
    x = sorted(x, key=None, reverse=True)
    for i in x:
        if i in db:
            db[i] += 1
        else:
            db[i] = 1
    return db

def double_count(x):
    db={}
    for i in x:
        for i2 in i:
            if i2 in db:
                db[i2] += 1
            else:
                db[i2] = 1
    db = sorted(db.items(), key=None, reverse=True)
    return db

def various_count(x):
    db={}
    for i in x:
        for i2 in i:
            if i2 in db:
                db[i2] += 1
            else:
                db[i2] = 1
    db = sorted(db.items(), key=None, reverse=True)
    return db

if __name__ == "__main__":
    try:
        x = sys.argv[1]
        x = x.split(',')
        if len(x)==1:
            x = letter_count(x)
        elif len(x)==2:
            x = double_count(x)
        else:
            x = various_count(x)

        o = ""
        for i in range(len(x)):
            if i<len(x):
                o+="%s:%d " % (x[i][0], x[i][1])
            else:
                o+="%s:%d" % (x[i][0], x[i][1])
        print(o)
    except Exception as e:
        print(e.args)
