class Solution(object):
    def totalFruit(self, fruits):
                start = 0
                max_len = float('-inf')
                adict = {}

                for end in range(len(fruits)):
                    if fruits[end] not in adict:
                        adict[fruits[end]] = 1
                    else:
                        adict[fruits[end]] += 1

                    while len(adict) > 2:
                        adict[fruits[start]] -= 1
                        if adict[fruits[start]] == 0:
                            del adict[fruits[start]]
                        start = start + 1

                    max_len = max(max_len, end - start + 1)

                if max_len == float('-inf'):
                    return 0
                else:
                    return max_len
