n = int(input())


for _ in range(n):
    
    nums = list(map(int,input().split()))
    str1 = list(input())
    str2 = list(input())
    ans = []
    flag = "".join(str1) < "".join(str2)
    k = nums[-1]
    str1.sort()
    str2.sort()
    
    s1 = s2 = 0
    a = b = 0
    while s1 < len(str1) and s2 < len(str2):
        
        if a == k:
            ans.append(str2[s2])
            s2 += 1
            a = 0
            b += 1
            continue
        if b == k:
            ans.append(str1[s1])
            s1 += 1
            a += 1
            b = 0
            continue
        
        if str1[s1] < str2[s2]:
            ans.append(str1[s1])
            s1 += 1
            a += 1
            b = 0
        else:
            ans.append(str2[s2])
            s2 += 1
            b += 1
            a = 0
            
    print(''.join(ans))
    
