class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        '''
            [1,4,2,5,3] => 5 => i = 1,3,5
            
            j -> (0, len(arr) - i + 1)
            ar[j:i]
            
            i = 1
            j=0 -> ar[0:1]
            
            i = 3
            j=0 -> ar[0:3]
            j=1 -> ar[1:4]
        
        '''
        
        currSum = 0
        for i in range(1, len(arr)+1, 2):
            for j in range(0, len(arr)-i + 1):
                currSum += sum(arr[j:j+i])
        
        return currSum