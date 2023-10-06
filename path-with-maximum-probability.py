class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        count = 0
        for s,e in edges:
            graph[s].append((e,succProb[count]))
            graph[e].append((s,succProb[count]))
            count += 1
        
        dist = [float("-inf") for i in range(n)]
        dist[start_node] = 1
        hp = [(-1,start_node)]
        visited = set()
        while hp:
            curr_dist , node = heappop(hp)
            curr_dist = abs(curr_dist)
            if node in visited:
                continue
            visited.add(node)

            for ch_node,w in graph[node]:
                temp = w * curr_dist
                if temp > dist[ch_node]:
                    dist[ch_node] = temp
                    heappush(hp,(-temp,ch_node))
        print(dist)
        return 0 if dist[end_node] == float("-inf") else dist[end_node]