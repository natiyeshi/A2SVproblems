class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        for i in range(len(queries)):
            queries[i] = Counter(queries[i])[min(queries[i])]
        for i in range(len(words)):
            words[i] = Counter(words[i])[min(words[i])]
        result = [0 for i in queries]
        for i in range(len(queries)):
            for j in words:
                if j > queries[i]:
                    result[i] += 1
        return result