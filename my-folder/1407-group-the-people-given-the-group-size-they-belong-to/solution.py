class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        # 2 1 3 3 3 2 2 2
        # 0 1 2 3 4 5 6 7
        
        # 1: [1], 2: [0,5,6,7], 3: [2,3,4]
        
        d = {}
        
        for i in range(len(groupSizes)):    
            groupSize = groupSizes[i]
            
            if groupSize not in d:
                d[groupSize] = [i]
            else:
                d[groupSize].append(i)
        
        res = []
        for groupSize, persons in d.items():
            for i in range(0, len(persons), groupSize):
                res.append(persons[i:i+groupSize])
        
        return res
