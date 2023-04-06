class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        temp = []
        is_prime = [True for i in range(right + 1)]
        is_prime[0] = is_prime[1] = False
        d = 2
        while d * d <= right:
            if is_prime[d]:
                j = d * d
                while j <= right:
                    is_prime[j] = False
                    j += d
            d += 1
        for i in range(left,right + 1):
            if is_prime[i]:temp.append(i)

        if len(temp) < 2: return [-1,-1]
        min_ = float("inf")
        result = [-1,-1]
        for i in range(len(temp) - 1):
            if temp[i + 1] - temp[i] < min_:
                result = [temp[i],temp[i+1]]
                min_ = temp[i + 1] - temp[i]

        return result