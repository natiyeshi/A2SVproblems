class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
         
        if len(people) < 2:
            return 1

        start = 0
        end = len(people) - 1
        counter = 0
        while start < end:
            if people[start] + people[end] <= limit:
                start += 1
                end -= 1
            else:
                end -= 1
            counter += 1
        if start == end:
            counter += 1
        return counter
