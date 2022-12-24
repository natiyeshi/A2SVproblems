class Solution(object):
    def average(self, salary):
        salary.sort()

        av = 0
        for ind,val in enumerate(salary):
            if ind != 0 and ind != len(salary) - 1:
                av += val
        
        average =  av / (len(salary) - 2.0)
        return average
        """
        :type salary: List[int]
        :rtype: float
        """
        