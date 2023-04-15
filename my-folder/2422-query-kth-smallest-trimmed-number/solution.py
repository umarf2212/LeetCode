import heapq
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        ans = []
        for query in queries:
            k = query[0]
            trim = query[1]

            trimmedNums = [(int(nums[i][len(nums[i])-trim:]), i) for i in range(len(nums))]
            
            heapq.heapify(trimmedNums)
            
            while k > 1:
                heapq.heappop(trimmedNums)
                k -= 1
            
            ans.append(trimmedNums[0][1])

        return ans

