class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingdom = defaultdict(list)
        self.kingName = kingName
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.deaths.add(name)
        pass

    def getInheritanceOrder(self) -> List[str]:
        result = []
        if self.kingName not in self.deaths:
            result.append(self.kingName)

        def dfs(parent):
            for i in self.kingdom[parent]:
                if i not in self.deaths:
                    result.append(i)
                dfs(i)

        dfs(self.kingName)
        return result


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()