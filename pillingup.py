# Enter your code here. Read input from STDIN. Print output to STDOUT

def pilling(block,s):
    j = s - 1
    i = 0
    before = None
    if blocks[i] < blocks[j]:
        before = blocks[j]
        j -= 1
    else:
        before = blocks[i]
        i += 1
    while i < j:
        if blocks[i] < blocks[j]:
            if before >= blocks[j]:
                before = blocks[j]
                j -= 1
            else:
                return "No"
        else:
            if before >= blocks[i]:
                before = blocks[i]
                i += 1
            else:
                return "No"
    return "Yes"

            
    
    
    

T = int(input())
for i in range(T):
    s = int(input())
    blocks = input().split(" ")
    blocks = list(map(int,blocks))
    print(pilling(blocks,s))
   

