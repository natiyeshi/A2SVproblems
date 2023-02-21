n1 = int(input())
nums1 = list(map(int,input().split()))
n2 = int(input())
nums2 = list(map(int,input().split()))

nums1.sort()
nums2.sort()

c1 = c2 = 0
counter = 0
while c1 < n1 and c2 < n2:
    
    if abs(nums1[c1] - nums2[c2]) < 2:
        counter += 1
        c1+=1
        c2+=1
    elif nums1[c1] > nums2[c2]:
        c2 += 1
    else:
        c1 += 1
print(counter)
