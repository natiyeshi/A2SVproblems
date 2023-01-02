num = int(input())

val = {"S":0,"L":100,"M":50}

for _ in range(num):
    t1 , t2 = input().split(" ")
    if val[t1[-1]] > val[t2[-1]]:
        print(">")
    elif val[t1[-1]] < val[t2[-1]]:
        print("<")
    else:
        if t1[-1] == "S":
            if len(t1) > len(t2):
                print("<")
            elif len(t1) < len(t2):
                print(">")
            else:
                print("=")
        else:
            if len(t1) > len(t2):
                print(">")
            elif len(t1) < len(t2):
                print("<")
            else:
                print("=")
            
