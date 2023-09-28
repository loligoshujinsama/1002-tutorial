#!usr/bin/env/python
import sys

def sum_iterative(x):
    sum = 0
    for i in range(1,x+1):
        sum += i
    return sum

def sum_recursive(x):
    if x == 1:
        return 1
    else:
        #Let x be 3; it will keep calling the function until 1
        return x + sum_recursive(x-1)


if __name__ == "__main__":
    try:
        x = int(sys.argv[1])
        print(f"The SUM value calculated by recursive is {sum_recursive(x)} and by iterative is {sum_iterative(x)}.")

    except Exception as e:
        print("Invalid input!")
