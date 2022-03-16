class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(nums1)):
            next = -1
            curr = False
            for j in range(len(nums2)):
                
                if curr and nums2[j] > nums1[i]:
                    next = nums2[j]
                    break
                
                if nums1[i] == nums2[j]:
                    curr = True
            
            ans.append(next)
        
        return ans
