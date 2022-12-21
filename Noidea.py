# Enter your code here. Read input from STDIN. Print output to STDOUT

nm = input()
arr = input().split()
A = input().split()
B = input().split()


print (sum([(i in A) - (i in B) for i in arr]))    
