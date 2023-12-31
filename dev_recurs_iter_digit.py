#!usr/bin/env/python
import sys

#Base case added on 1:55AM 29/09/2023, in the case of digit_i(1). It should return a 1.
def digit_i(x):
    c = 0
    if x < 10:
        return 1
    else:
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
