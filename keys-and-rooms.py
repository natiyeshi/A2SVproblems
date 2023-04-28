class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set(rooms[0])
        visited.add(0)
        que = deque(rooms[0])      
        while que:
            nodes = rooms[que.popleft()]
            print(nodes,visited)
            for i in nodes:
                if i not in visited:
                    visited.add(i)
                    que.append(i)
        
        return len(visited) == len(rooms)