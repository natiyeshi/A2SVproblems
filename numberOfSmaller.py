i , j = list(map(int,input().split()))

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

main = []
ptra = ptrb = 0
c = 0

for _ in range(j):
    if ptra >= i:
        break
    # print(arr2[ptrb],arr1[ptra])
    while arr2[ptrb] > arr1[ptra]:
        c += 1
        ptra += 1
        if ptra >= i: 
            break
 
    main.append(c) 
    ptrb += 1
    
    
for i in range(ptrb,j):
    main.append(main[-1])
    
print(" ".join(list(map(str,main))))

