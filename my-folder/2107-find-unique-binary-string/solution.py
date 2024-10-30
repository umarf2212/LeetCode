class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def backtrack(binaryArray, ind, result, numsSet):
            if ind == len(binaryArray):
                num = ''.join(binaryArray)
                if num not in numsSet:
                    result.append(num)
                return
            
            if len(result) > 0:
                return
            
            backtrack(binaryArray, ind+1, result, numsSet)

            binaryArray[ind] = '1'
            backtrack(binaryArray, ind+1, result, numsSet)
            binaryArray[ind] = '0'
        
        numsSet = set(nums)
        n = len(nums[0])
        binaryArray = ['0'] * n
        result = []
        backtrack(binaryArray, 0, result, numsSet)

        return result[0]
