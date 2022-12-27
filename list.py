

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        st = input().split(" ")
        if st[0] == "insert":
            arr.insert(int(st[1]),int(st[2]))
        elif st[0] == "print":
            print(arr)
        elif st[0] == "remove":
            arr.remove(int(st[1]))
        elif st[0] == "append":
            arr.append(int(st[1]))
        elif st[0] == "sort":
            arr.sort()
        elif st[0] == "pop":
            arr.pop()
        elif st[0] == "reverse":
            arr.reverse()
            
            
