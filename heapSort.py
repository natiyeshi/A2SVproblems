#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapifyPush(self,heap,val):
        heap.append(val)
        self.heapifyUp(heap,len(heap) - 1)
    def heapifyUp(self,heap,curr):
        par = (curr - 1) // 2
        if curr > 0 and heap[par] > heap[curr]:
            heap[par] , heap[curr] = heap[curr] , heap[par]
            self.heapifyUp(heap,par)
        
    #Function to build a Heap from array.
    def heapPop(self,heap):
        heap[0] , heap[-1] = heap[-1] , heap[0]
        temp = heap.pop()
        self.heapifyDown(heap,0)
        return temp
    def heapifyDown(self,heap,curr):
        left = 2 * curr + 1
        right = 2 * curr + 2
        
        if left >= len(heap):
            return
        elif right >= len(heap) :
            if heap[left] >= heap[curr]: return
            heap[left],heap[curr] = heap[curr],heap[left]
            self.heapifyDown(heap,left)
        else:
            temp = left if heap[left] < heap[right] else right
            if heap[temp] >= heap[curr]: return
            heap[temp],heap[curr] = heap[curr],heap[temp]
            self.heapifyDown(heap,temp)
        
    def HeapSort(self, arr, n):
        heap = []
        for i in arr:
            self.heapifyPush(heap,i)
        for i in range(len(arr)):
            arr[i] = self.heapPop(heap)
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends
