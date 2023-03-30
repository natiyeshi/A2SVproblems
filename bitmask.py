from collections import Counter , defaultdict
from bisect import bisect_left , bisect_right

import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inlint():
    temp =list(map(int,list(input())[:-1]))
    return temp
def init(): 
    return(int(input()))
def inlst():
    return(list(map(int,input().split())))
def inchar():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def instr():
    return(input().split())



def solve(num):
    result = ["1"]
    num >>= 1
    while True:
        if num & 1 == 1:
            result.append("1")
            num >>= 1
            break
        else:
            result.append("0")
        num >>= 1
    if num > 0:
        result[0] = "0"
    result.reverse()
    return int("".join(result),2)


test = init()
"""11011111101010010"""
for i in range(test):
    num = init()
    if num == 1:
        print(3)
        continue
    if num & 1: 
        print(1)
        continue
    print(solve(num))
