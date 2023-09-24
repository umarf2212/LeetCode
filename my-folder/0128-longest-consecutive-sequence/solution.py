class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        streak = 1
        for num in nums:
            # num is the start of a new sequence
            if num-1 not in s:

                curLongest = 1
                curNum = num

                while curNum+1 in s:
                    curLongest += 1
                    curNum += 1
                
                streak = max(streak, curLongest)
        
        return streak


