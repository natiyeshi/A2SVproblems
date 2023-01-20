r,c = list(map(int,input().split()))

mat = []

for i in range(r):
    temp = list(input())
    mat.append(temp)

row = []
col = []


for i in range(len(mat)):
    val = set()
    for j in range(len(mat[i])):
        
        if mat[i][j] in val:
            row.append([i,mat[i][j]])
        else:
            val.add(mat[i][j])
for i in range(len(mat[0])):
    val = set()
    for j in range(len(mat)):
        
        if mat[j][i] in val:
            col.append([i,mat[j][i]])
        else:
            val.add(mat[j][i])
        

for itr in row:
    for i in range(c):
        if mat[itr[0]][i] == itr[1]:
            mat[itr[0]][i] = "."
for itr in col:
    for i in range(r):
        if mat[i][itr[0]] == itr[1]:
            mat[i][itr[0]] = "."
        
string = []
for i in mat:
    for j in i:
        if j != ".":
            string.append(j)
print("".join(string))        
   
   
