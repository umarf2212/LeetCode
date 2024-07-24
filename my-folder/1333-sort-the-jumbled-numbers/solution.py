class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        numMapping = [0] * 10
        for i in range(0, 10):
            numMapping[i] = mapping[i]

        def convertToMap(num, numMapping):
            num = str(num)
            res = 0
            for n in num:
                res = res * 10 + numMapping[int(n)]
            
            return res
        
        numMapPairs = []
        for i, num in enumerate(nums):
            numMapPairs.append([num, convertToMap(num, numMapping), i])
        
        numMapPairs.sort(key=lambda x:(x[1], x[2]))

        return [num[0] for num in numMapPairs]


