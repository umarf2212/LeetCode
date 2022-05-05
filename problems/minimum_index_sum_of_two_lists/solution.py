class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        
        d1 = {}
        for i in range(len(list1)):
            d1[list1[i]] = i
        
        minSum = float('inf')
        res = []
        for i in range(len(list2)):
            if list2[i] in d1:
                currSum = d1[list2[i]] + i
                if currSum < minSum:
                    minSum = currSum
                    res = [list2[i]]
                
                elif currSum == minSum:
                    res.append(list2[i])


        return res