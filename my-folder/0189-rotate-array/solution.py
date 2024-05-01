class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = 3

        # 1 2 3 4 5 6 7 => 5 6 7 1 2 3 4
        # 7 6 5 | 4 3 2 1
        # 5 6 7 | 1 2 3 4

        # k = 0
        # 1 2 3 4 5
        # 5 4 3 2 1
        # arr[:0], ar[0:]

        # k = 7 % n
        # 1 2 3 4 5
        # 4 5 1 2 3

        n = len(nums)
        k = k % n


        # 1 2 | 3 4 5 6 | 7 8

        def reverseSubarray(ar, i, j):
            while i < j:
                ar[i], ar[j] = ar[j], ar[i]
                i += 1
                j -= 1
        
        # 1. Reverse the whole array
        reverseSubarray(nums, 0, n-1)

        # 2. Reverse first K elements
        reverseSubarray(nums, 0, k-1)

        # 3. Reverse last n-k elements
        reverseSubarray(nums, k, n-1)





