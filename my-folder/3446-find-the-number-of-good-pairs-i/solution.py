class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        m = len(nums1)
        n = len(nums2)

        for i in range(n):
            nums2[i] = nums2[i]*k

        goodPairCount = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] % nums2[j] == 0:
                    goodPairCount += 1
        
        return goodPairCount


