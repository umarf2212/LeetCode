from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        arrCount = Counter(arr)
        targetCount = Counter(target)
        
        for num in targetCount.keys():
            if num not in arrCount or arrCount[num] != targetCount[num]:
                return False
        return True

            

