class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        missing = [i for i in range(1, arr[0])]
        
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] > 1:
                ar = [i for i in range(arr[i-1]+1, arr[i])]
                missing += ar
                
        if k > len(missing)-1:
            missing += [i for i in range(arr[len(arr)-1]+1, arr[len(arr)-1]+k+1)]            
                
        return missing[k-1]