class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        counter = {}
        maxFreq = 0
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
            maxFreq = max(maxFreq, counter[num])
        
        return sum([count for count in counter.values() if count==maxFreq])
