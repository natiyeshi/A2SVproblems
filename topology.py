from typing import List


from typing import List

from collections import defaultdict,deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        
        temp = defaultdict(int)
        
        graph = defaultdict(set)
        e = defaultdict(int)
        
        for f,t in edges:
            graph[f].add(t)
            e[t] += 1
        
        que = deque()
        
        for i in range(1,n + 1):
            if e[i] == 0:
                que.append(i)
        
        counter = 1
        
        while que:
            level = len(que)
            for _ in range(level):
                node = que.popleft()
                temp[node] = counter  
                for i in graph[node]:
                    e[i] -= 1
                    if e[i] == 0:
                        que.append(i)
            counter += 1
        
        result = [str(temp[i]) for i in range(1,n + 1)]
        result = " ".join(result)
        return result
                    
        
        
        
        
        # code here
            


