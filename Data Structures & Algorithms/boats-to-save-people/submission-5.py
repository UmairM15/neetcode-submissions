class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boatCount = 0
        people.sort()
        i, j = 0, len(people) - 1
        
        while i < j:
            totalWeight = people[j] + people[i]

            if people[j] >= limit or totalWeight > limit:
                boatCount += 1
                j -= 1
            else:
                boatCount += 1
                i += 1
                j -= 1
        
        return boatCount if i > j else boatCount + 1