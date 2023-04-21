class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()

        def dfs(ind):
            if ind in visited:
                return
            visited.add(ind)
            for val in rooms[ind]:
                dfs(val)
        dfs(0)
        return len(visited) == len(rooms)