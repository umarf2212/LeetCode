from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        d = Counter(nums)
        minCount = 0
        seen = set()

        for num, count in d.items():

            x = k - num

            if x in seen:
                continue

            if x == num:
                minCount += count//2
            
            elif x in d:
                minCount += min(count, d[x])
                seen.add(num)
        
        return minCount

'''
        [2,2,2,3,1,1,4,1]

        1:3
        2:3
        3:1
        4:1

'''
