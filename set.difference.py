# Enter your code here. Read input from STDIN. Print output to STDOUT

def cal(a,la,b,lb):
    c = 0
    for i in la:
        if i not in lb:
            c += 1
    print(c)
    
    
a = int(input())
la = input().split(" ")
b = int(input())
lb = input().split(" ") 
map(int,la)
map(int,lb)


cal(a,la,b,lb)
