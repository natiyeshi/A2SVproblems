#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(arr):
    c = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1] ,arr[j]
                c += 1
                # Write your code here
    print("Array is sorted in " +str(c)+" swaps.")
    print("First Element: "+str(arr[0]))
    print("Last Element: "+str(arr[-1]))
    
    
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
