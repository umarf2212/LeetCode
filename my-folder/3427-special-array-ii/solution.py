class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        # 1. Divide the array into several special subarrays
        # 2. For each query, check if it falls within a subarray.

        # returns True if a and b's parities are different
        # false otherwise
        def checkParity(a, b):
            if a%2 == 0 and b%2 == 0:
                return False
            
            if a%2 != 0 and b%2 != 0:
                return False
            
            return True

        i = 0
        specialSubarrays = [] # ranges of special subarrays
        for j in range(len(nums)-1):
            if checkParity(nums[j], nums[j+1]):
                continue
            
            # j and j+1 have same parity
            # [i, j] is a special subarray
            # next special subarray would start from j+1

            specialSubarrays.append([i, j])
            i = j+1
        
        specialSubarrays.append( [i, len(nums)-1] )

        print(specialSubarrays)

        result = []
        for query in queries:
            a, b = query
            cur = False
            
            lo = 0
            hi = len(specialSubarrays)-1
            while lo <= hi:
                mid = (lo+hi) // 2
                c, d = specialSubarrays[mid]

                if c <= a:
                    lo = mid+1
                else:
                    hi = mid-1
            
            c, d = specialSubarrays[hi]
            if a >= c and b <= d:
                cur = True

            # replacing linear search with Binary Search above
            # for i in range(len(specialSubarrays)):
            #     c, d = specialSubarrays[i]

            #     if a >= c and b <= d:
            #         cur = True
            #         break
            
            result.append(cur)
        
        return result
        
        # 1 2 3 4 5 
        # 1 2 3 4 5 6

        # 1 2 3 | 1 4 5

        # 1 2 3 | 1 | 1 4

        # Overlap check
        # [1, 4] [2, 7]


                
