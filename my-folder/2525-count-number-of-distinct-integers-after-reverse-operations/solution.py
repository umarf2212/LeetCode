class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        S = set()
        for num in nums:
            rev = int(str(num)[::-1])
            S.add(num)
            S.add(rev)
        
        return len(S)

