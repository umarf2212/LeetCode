import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        operations = 0
        while len(nums) >= 2:
            if nums[0] >= k:
                break

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            val = min(x, y) * 2 + max(x, y)

            heapq.heappush(nums, val)
            operations += 1
        

        return operations
