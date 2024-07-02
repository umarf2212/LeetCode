from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for num in nums1:
            d1[num] += 1
        
        for num in nums2:
            d2[num] += 1
        
        res = []
        for num, count in d1.items():
            if num in d2:
                res += [num] * min(count, d2[num])
        
        return res
