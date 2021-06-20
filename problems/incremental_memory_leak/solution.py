class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
        i=1
        
        while i <= memory1 or i <= memory2:
            
            if memory1 > memory2 and memory1 >= i:
                memory1 -= i
            elif memory2 > memory1 and memory2 >= i:
                memory2 -= i
            elif memory1 == memory2 and memory1 >= i:
                memory1 -= i
                
            i+=1
        
        return [i, memory1, memory2]
            
        
        '''
        
        1 -> 8
        2 -> 11
        
        i = 1
        2 -> 11-1 = 10
        
        i=2
        2 -> 10-2 = 8
        
        i=3
        1 -> 8-3 = 5
        
        i=4
        2 -> 8-4 = 4
        
        i=5
        1 -> 5-5 = 0
        
        i=6
        i > '1' (0) and i > '2' (4)
        
        
        '''