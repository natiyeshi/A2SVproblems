

for _ in range(1):
    length = int(input())
    string = list(map(int,input().split()))
    string.sort()
    counter = 0
    if string[0] >= 0:
        for i in range(length):
            if string[i] == 0:
                counter += 1
                continue
            counter += string[i] - 1
        print(counter)
    elif string[-1] <= 0:
        for i in range(length):
            if i == length - 1 and length % 2 != 0:
                counter += 1 - string[length - 1]
                continue
            if string[i] == 0:
                counter += 1
                continue
            counter += abs(string[i]) - 1
        print(counter)
    else:
        c = 0
        for i in range(length):
            if string[i] <= 0:
                c += 1
            else:
                break
            
        if c % 2 == 0:
            for i in range(c):
                if string[i] == 0:
                    counter += 1
                    continue
                counter += abs(string[i]) - 1
            for i in range(c,length):
                if string[i] == 0:
                    counter += 1
                    continue
                counter += string[i] - 1
            print(counter)
        else:
            for i in range(c - 1):
                if string[i] == 0:
                    counter += 1
                    continue
                counter += abs(string[i]) - 1
            counter += 1 - string[c-1]
            for i in range(c,length):
                if string[i] == 0:
                    counter += 1
                    continue
                counter += string[i] - 1
            print(counter)
            
    
