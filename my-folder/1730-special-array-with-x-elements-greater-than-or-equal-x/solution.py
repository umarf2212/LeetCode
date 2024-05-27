class Solution:
    def specialArray(self, nums: List[int]) -> int:

        '''
        1 2 3 4 5
        0 1 2 3 4

        # 1. Sort the array.
        # 2. X ranges between 0 and len(nums)
        # 3. For every X, count numbers that are >= X

        1 4 2 8 5 7
        1 2 4 5 7 8

        1 2 3 4 5
        0 1 2 3 4

        5 6 7 8 => 4
        1 6 7 8 => 3
        '''
        
        n = len(nums)
        nums.sort()

        for i in range(1, n+1):
            count = 0
            for j in range(n-1, -1, -1):
                if nums[j] >= i:
                    count += 1
            
            if count == i:
                return i

        return -1
        




