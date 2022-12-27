# Enter your code here. Read input from STDIN. Print output to STDOUT

def ch(A,arr):
    # print(A,arr)
    for j in arr:
        if len(j) >= len(A):
            return False 
        for i in j:
            if i not in A:
                return False
    return True
    

A = input().split(" ")
A = list(map(int,A))
n = int(input())
arr = []
for _ in range(n):
    t = input().split(" ")
    t = list(map(int,t))    
    arr.append(t)        
print(ch(A,arr))
