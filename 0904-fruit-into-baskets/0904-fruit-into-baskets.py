class Solution(object):
    def totalFruit(self, fruits):
        dic = defaultdict(int)
        left = 0
        result = 0
        for i in range(len(fruits)):
            dic[fruits[i]] += 1
            while len(dic) > 2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    del dic[fruits[left]]
                left += 1
            result = max(result,i - left + 1)
        return result
        """
        :type fruits: List[int]
        :rtype: int
        """
        