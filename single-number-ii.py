class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def sumBin(a,b = ""):
            l = 0
            if len(b) > len(a): lar ,sm= b,a
            else: lar ,sm= a,b
            s = [] 
            for i in range(len(lar) - len(sm)):
                s.append("0")
            sm = s + sm
            result = lar.copy()
            for i in range(len(lar)):
               temp = int(sm[i]) + int(lar[i])
               result[i] = str(temp)
            return result 
        ans = []
        flag = min(nums)
        for i in range(len(nums)): nums[i] += abs(flag)
        for i in nums:
            ans = sumBin(ans,list(bin(i)[2:]))
        result = []
        for i in ans:
            if int(i) % 3 != 0:result.append("1")
            else:result.append("0")
        return int("".join(result),2) - abs(flag)