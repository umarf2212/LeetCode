import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        q = [-int(num) for num in nums]

        heapq.heapify(q)

        while k > 1:
            heapq.heappop(q)
            k -= 1
        
        return str(-q[0])
        