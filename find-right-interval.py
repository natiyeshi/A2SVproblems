class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        temp = []
        c = 0
        for itr in intervals:
            temp.append([itr[0],c])
            c += 1
        temp.sort()
        ind = []
        search = []
        result = []
        for t in temp:
            ind.append(t[1])
            search.append(t[0])
        for _,val in intervals:
            t = bisect_left(search,val)
            if len(search) <= t:
                result.append(-1)
            else:
                result.append(ind[t])

        return result