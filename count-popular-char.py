import sys


if __name__ == "__main__":
    try:
        string = sys.argv[1]
        string = string.lower()
        new_list = sorted(string, key=None, reverse=False)

        counter = {}

        for i in new_list:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        #Sort dictionary based on counter[x][1] (Number of occurences)
        counter = sorted(counter.items(), reverse=True, key=lambda item: item[1])


        output=""
        for i in range(5):
            if i==4:
                output+=str(counter[i][0])+":"+str(counter[i][1])
            else:
                output+=str(counter[i][0])+":"+str(counter[i][1])+","
        print(output)
    except Exception as e:
        #print(e)
        print("Invalid input")