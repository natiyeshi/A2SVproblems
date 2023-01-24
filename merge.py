i , j = list(map(int,input().split()))

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
main = []

ptra = ptrb = 0
for _ in range(i + j):
  
    if ptra == i:
        main.append(arr2[ptrb])
        ptrb += 1
        continue
    
    if ptrb == j:
        main.append(arr1[ptra])
        ptra += 1
        continue
    
    if arr1[ptra] >= arr2[ptrb]:
        main.append(arr2[ptrb])
        ptrb += 1
    else:
        main.append(arr1[ptra])
        ptra += 1
    

print(" ".join(list(map(str,main))))
        
        
