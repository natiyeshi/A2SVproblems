class Solution(object):
    def average(self, salary):
        salary.sort()

        return sum(salary[1:-1]) / (len(salary) - 2.0) 
       
        """
        :type salary: List[int]
        :rtype: float
        """
        