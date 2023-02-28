class Solution:
    def getRow(self, rowIndex, arr = [1,1]) -> List[int]:
        if rowIndex <= 0:
            return [1]
        if rowIndex == 1:
            return arr
        newArr = [1]
        left = 0
        while left < len(arr) - 1:
            newArr.append(arr[left] + arr[left + 1])
            left += 1
        newArr.append(1)
        return self.getRow(rowIndex - 1,newArr)