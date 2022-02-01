class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def search(x):
            lo = 0
            hi = len(nums1)-1
            while lo <= hi:
                mid = (lo+hi)//2
                if nums1[mid] == x: 
                    return True
                elif nums1[mid] < x:
                    lo = mid+1
                else:
                    hi = mid-1
            return False
        
        nums1.sort()
        res = set()
        for num in nums2:
            if search(num):
                res.add(num)
        
        return list(res)