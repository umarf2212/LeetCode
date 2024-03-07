class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        # n = 7 
        # 15 10 10

        # 7 + 10 = 17 // 2 = 8

        # 0 1 2 3 4 5 6
        # 5 5 5 5 5 5 5
        # 4 6 5 5 5 5 5

        # n = 6
        # 11 6

        # 0 1 2 3 4 5
        # 2 3 3 3 3 3 

        # Minimum items that can be given = 1
        # At least 1 unit of 1 type of item can be given 
        # to 1 store.

        # Maximum: we can give at most max(quantities) to one store
        # i.e. all items of one type to one store

        def canDistribute(k):
            count = 0
            for items in quantities:
                count += (items-1) // k + 1
            
            if count > n:
                return False
            return True

        lo = 1
        hi = max(quantities)
        while lo < hi:
            mid = (lo+hi) // 2

            if canDistribute(mid):
                hi = mid
            else:
                lo = mid+1
        
        return lo
        




