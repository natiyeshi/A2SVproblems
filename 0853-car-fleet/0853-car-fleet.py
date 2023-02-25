class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        time = []
        for i in range(len(position)):
            time.append( ( target - position[i] ) / speed[i])
            dic[int(position[i])] = time[i]
        position.sort()
        stack = []
        
        for p in position:
            while stack and dic[p] >= stack[-1]:
                stack.pop()
            stack.append(dic[p])
        return len(stack)