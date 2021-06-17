class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        d = set()
        dups = set()
        
        for num in nums:
            if num in d:
                dups.add(num)
                d.remove(num)
            elif num not in dups:
                d.add(num)
        
        return sum(d)