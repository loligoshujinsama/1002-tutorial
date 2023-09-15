import sys

def difference(a):
    sum=0
    for i in range(len(a)):
        if i==0:
            sum+=a[i]
        elif i==(len(a)-1):
            sum-=a[i]
    return sum

def even_odd_count(a):
    even = 0
    odd = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            even+=1
        else:
            odd+=1
    return even, odd

def even_odd_sum(a):
    even = 0
    odd = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            even+=a[i]
        else:
            odd+=a[i]
    return odd, even

def centered_avg(a):
    avg=[]
    avg2=0
    for i in range(len(a)):
        if i==0:
            pass
        elif i==(len(a)-1):
            pass
        else:
            avg.append(a[i])
            avg2+=a[i]
    avg2=int(avg2/len(avg))
    return avg2


if __name__ == "__main__":
    try:
        input = sys.argv[1]
        input = input.split(',')
        input_int=[]
        for i in input:
            input_int.append(int(i))

        input_int = sorted(input_int, reverse=True)

        print(f"The sum of all even numbers is {even_odd_sum(input_int)[1]}, the sum of all odd numbers is {even_odd_sum(input_int)[0]}, the difference between the biggest and smallest number is {difference(input_int)}, the total number of even numbers is {even_odd_count(input_int)[0]}, the total number of odd numbers is {even_odd_count(input_int)[1]}, the centered average is {centered_avg(input_int)}.")
        
    #except ValueError:
    except Exception as e:
        print("Please enter valid integers.")


