from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        # a-b = k
        # a = k+b

        # 1 1 3 3 3 4 5 6 8 10 12 15 18
        # nums.sort()
        
        S = Counter(nums)
        count = 0

        if k == 0:
            for val in S.values():
                if val >= 2:
                    count += 1
        else:
            SK = set([i+k for i in nums])
            for num in S:
                if num in SK:
                    count+=1

        return count