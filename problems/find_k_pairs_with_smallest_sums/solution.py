import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))

        res = []
        while heap and k > 0:

            _, n1, n2, ind = heapq.heappop(heap)
            res.append([n1, n2])

            if ind+1 < len(nums2):
                heapq.heappush(heap, (n1+nums2[ind+1], n1, nums2[ind+1], ind+1))

            k-=1
        
        return res