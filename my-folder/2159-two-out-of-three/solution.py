class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        d1 = set(nums1)
        d2 = set(nums2)
        d3 = set(nums3)
        
        result = []
        
        nums = list(set(nums1+nums2+nums3))
        
        for num in nums:
            if num in d1 and num in d2 or\
            num in d1 and num in d3 or\
            num in d2 and num in d3:
                result.append(num)
        
        return result
