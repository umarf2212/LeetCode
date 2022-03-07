class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        refill = capacity
        
        steps = 0
        for i in range(len(plants)):
            if capacity >= plants[i]:
                steps += 1
            else:
                steps += 2*i + 1
                capacity = refill
            
            capacity -= plants[i]
        
        return steps