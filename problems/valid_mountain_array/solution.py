class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3: return False
        
        # prev = arr[0]
        
        i=1
        while arr[i] > arr[i-1]:
            i+=1
            if i == len(arr): return False
        
        j = len(arr)-1
        while arr[j-1] > arr[j]:
            j-=1
            if j == 0: return False
        
        if i-1 == j:
            return True