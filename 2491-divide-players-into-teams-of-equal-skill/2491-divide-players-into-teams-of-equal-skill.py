class Solution(object):
    def dividePlayers(self, skill):
        
        skill.sort()
        
        start = 0
        end = len(skill) - 1
        
        val = None
        sum_ = 0
        while start < end:
            curr =  skill[start] + skill[end]
            sum_ += skill[start] * skill[end]
            if val is None:
                val = curr
            else:
                 if val != curr:
                    return -1
            start += 1
            end -= 1
        return sum_
                
        
        """
        :type skill: List[int]
        :rtype: int
        """
        