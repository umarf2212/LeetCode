class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        counts = {}
        
        nums.sort(reverse=True)
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        
        ar = []
        for num, count in counts.items():
            ar.append([num, count])
            
        ar.sort(key=lambda x: x[1])
        
        res = []
        for num in ar:
            res += [num[0]] * num[1]
        
        return res