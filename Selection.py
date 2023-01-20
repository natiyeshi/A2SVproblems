#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    
    def selectionSort(self, arr,n):
        
        for i in range(n):
            ind = i
            small = arr[i]
            for j in range(i,n):
                if arr[j] < small:
                    small = arr[j]
                    ind = j
            if ind != i:
                arr[ind], arr[i] = arr[i], arr[ind]
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
