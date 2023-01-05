class Solution(object):
    def subdomainVisits(self, cpdomains):
        dic = defaultdict(int)
        
        for ele in cpdomains:
            num , string = ele.split(" ")
            strings = string.split(".")
            for i in range(len(strings) - 1,-1,-1):
                temp = ".".join(strings[i:])
                dic[temp] += int(num)
        ans = []
        for i in dic:
            temp = str(dic[i]) + " "+str(i)
            ans.append(temp)
        return ans
        
        
        
        
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        