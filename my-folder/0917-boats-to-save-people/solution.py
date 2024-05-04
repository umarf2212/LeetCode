import heapq
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # 1 2 3 3 7 6 4 5
        
        # 1 2 3 3 4 5 6 7

        people.sort()

        count = 0
        i = 0
        j = len(people)-1
        while i < j:

            if people[i] + people[j] > limit:
                count += 1
                j -= 1
            else:
                i += 1
                j -= 1
                count += 1
        
        if i == j:
            count += 1

        return count

        # 1 2 2 3
        # 3





