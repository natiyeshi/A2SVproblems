class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        emails = defaultdict(set)
        persons = defaultdict(str)
        for item in accounts:
            temp = item[1:]
            for i in range(len(temp)):
                for j in range(i,len(temp)):
                    emails[temp[i]].add(temp[j])
                    emails[temp[j]].add(temp[i])
                persons[temp[i]] = (item[0])
        result = []
        visited = set()
        def dfs(k):
            if k in visited:
                return
            visited.add(k)
            result.append(k)
            for i in emails[k]:
                if i not in visited:
                    dfs(i)
        ans = []

        for i in emails:
            if i not in visited:
                dfs(i)
                result.sort()
                ans.append([persons[i]] + result)
            result = []

        return ans