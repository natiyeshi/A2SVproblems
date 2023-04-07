class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck.sort()
        def primes(num):
            pr = [True for i in range(num + 1)]
            pr[0] = pr[1] = False
            d = 2
            while d <= num:
                if pr[d]:
                    j = d + d
                    while j <= num:
                        pr[j] = False
                        j += d
                d += 1
            return [i for i in range(len(pr)) if pr[i]]
        def find(min_):
            i = 0
            while i < len(deck) - 1:
                if i + min_ - 1 >= len(deck) or deck[i] != deck[i + min_ - 1]:
                    return False   
                i += min_
            return True
        temp = list(Counter(deck).values())
        min_ = min(temp)
        mins = primes(min_)
        for i in mins:
            if find(i): return True
        return  False