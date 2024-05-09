from heapq import heappush, heappop, heapify
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        # 1 2 3
        # k = 3

        happiness.sort(reverse=True)

        res = 0
        i = 0
        while i < k and i < len(happiness):
            cur = happiness[i]
            
            if cur - i >= 0:
                cur -= i
            else:
                cur = 0

            res += cur

            i += 1
        
        return res
