from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        counts = Counter(nums)
        countsArray = [[num, count] for num, count in counts.items()]
        countsArray.sort(key=lambda x:x[1])
        result = []
        for num, count in sorted(countsArray, key=lambda x:(x[1], -x[0])):
            result += [num] * count
        
        return result
