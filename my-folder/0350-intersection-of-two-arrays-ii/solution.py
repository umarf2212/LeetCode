class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        
        res = []
        for num, count in n2.items():
            if num in n1:
                numCount = min(count, n1[num])
                res += [num for _ in range(numCount)]
        
        return res
        
        
        
