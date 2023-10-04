class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        cost = []
        for i,arr in enumerate(costs):
            cost.append((arr[0],i,'a',arr[0] - arr[1]))
            cost.append((arr[1],i,'b',arr[1] - arr[0]))
        cost = sorted(cost,key=lambda a:(a[-1],a[0]))
        a,b = [],[]
        visited = set()
        for val,ind,city,_ in cost:
            if ind in visited:
                continue
            if city == 'a' and len(a) < len(costs) // 2:
                visited.add(ind)
                a.append(val)  
            if city == 'b' and len(b) < len(costs) // 2:
                visited.add(ind)
                b.append(val)
        print(a,b)
        print(cost)
        return sum(a)+sum(b)