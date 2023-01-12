class Solution(object):
    def moveZeroes(self, arr):
        bools = True
        counter = 0
        while(bools == True):
                bools = False
                print("hi")
                for  i in range(len(arr)):
                    if arr[i] == 0:
                        arr.pop(i)
                        counter += 1
                        bools = True
                        break
        [arr.append(0) for i in range(counter)]
        return arr
