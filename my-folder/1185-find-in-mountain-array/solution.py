# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # 1. Find peak element
        # 2. Divide array in 2 parts - increasing and decreasing
        # 3. First Binary Search target in increasing part
        # 4. If not found, then in decreasing part
        # 5. If not found, return -1

        def findPeak(arr):
            i = 0
            j = arr.length()-1
            while i <= j:
                mid = (i+j)//2

                midEl = arr.get(mid)
                leftEl = arr.get(mid-1) if mid>0 else -1
                RightEl = arr.get(mid+1) if mid < arr.length()-1 else -1

                if midEl > leftEl and midEl > RightEl:
                    return mid

                if mid < arr.length()-1 and leftEl < midEl < RightEl:
                    i = mid+1
                else:
                    j = mid-1
            
            return mid
        
        def binarySearch(arr, i, j, target, asc):
            compare = (lambda x, y: x > y) if asc else (lambda x, y: x < y)

            while i <= j:
                mid = (i+j)//2

                if arr.get(mid) == target:
                    return mid
                
                if compare(arr.get(mid), target):
                    j = mid-1
                else:
                    i = mid+1
            
            return -1
        
        peak = findPeak(mountainArr)
        
        left = binarySearch(mountainArr, 0, peak, target, True)
        if left != -1:
            return left

        right = binarySearch(mountainArr, peak+1, mountainArr.length()-1, target, False)
        return right


                
                
