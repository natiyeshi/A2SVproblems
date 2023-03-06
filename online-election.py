class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):  
        self.persons = persons
        self.times = times
        pre_count = 1
        winner = [persons[0]]
        counter = defaultdict(int)
        counter[persons[0]] = 1
        for i in range(1,len(persons)):
            counter[persons[i]] += 1
            if counter[persons[i]] >= pre_count:
                winner.append(persons[i])
                pre_count = counter[persons[i]]
            else:
                winner.append(winner[-1])
        self.winner = winner
        

    def q(self, t: int) -> int:
        ind = bisect_left(self.times,t)
        if ind >= len(self.times) or self.times[ind] != t: 
            ind -= 1 
        
        return self.winner[ind]
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)