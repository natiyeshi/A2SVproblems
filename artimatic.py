class Solution(object):
    def checkArithmeticSubarrays(self, nums, fr, to):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        dic = {}
        ret = []
        for i in range(len(fr)):
            dic[i] = nums[fr[i]:to[i] + 1]
        print(dic)
        for j in dic:
            bool = True
            dic[j].sort()
            dif = dic[j][0] - dic[j][1]
            for k in range(1,len(dic[j])):
                if dic[j][k - 1] - dic[j][k] != dif:
                    bool = False
                    break
            if bool == False: dic[j][-1] = False
            else: dic[j][-1] = True
        [ret.append(dic[i][-1]) for i in dic]       
        return ret
    
   
