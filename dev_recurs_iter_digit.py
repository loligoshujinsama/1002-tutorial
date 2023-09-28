#!usr/bin/env/python
import sys

def digit_i(x):
    c = 1
    while True:
        x = x//10
        if x <10:
            c += 1
            break
        else:
            c += 1
    return c

def digit_r(x):
    y = 1
    if x < 10:
        return 1
    else:
        return y + digit_r(x//10)
        


if __name__ == "__main__":
    try:
        x = int(sys.argv[1])
        print(f"The number of digit(s) calculated by recursive is {digit_r(x)} and by iterative is {digit_i(x)}.")

    except Exception as e:
        print("Invalid input!")
