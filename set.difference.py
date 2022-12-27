# Enter your code here. Read input from STDIN. Print output to STDOUT

    
a = int(input())
la = input().split(" ")
b = int(input())
lb = input().split(" ") 
la = set(map(int,la))
lb = set(map(int,lb))

oe = la.difference(lb)
print(len(oe))
