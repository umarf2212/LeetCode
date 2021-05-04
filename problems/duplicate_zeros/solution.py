class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        temp = 0
        1 0 0 2 3 0 5 0
        """
        temp = deque()
        i=0
        while i < len(arr):
            
            if temp:
                temp.append(arr[i])
                arr[i] = temp.popleft()
                                
            if arr[i] == 0:
                try:
                    temp.append(arr[i+1])
                    arr[i+1] = 0
                    i+=1
                except IndexError:
                    break
            
            i+=1

        
        return None