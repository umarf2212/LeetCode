class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        changes = [0, 0]
        for bill in bills:
            if bill == 5:
                changes[0] += 1
            
            elif bill == 10:
                if changes[0] == 0:
                    return False
                
                changes[0] -= 1
                changes[1] += 1
            
            elif bill == 20:
                if changes[1] > 0 and changes[0] > 0:
                    changes[0] -= 1
                    changes[1] -= 1
                
                elif changes[0] >= 3:
                    changes[0] -= 3

                else:
                    return False
                
        
        return True


        # [5,5,10,10,20]

        # 5 => +5
        # 5 => +5 +5
        # 10 => -5 +5 +10
        # 10 => -5 -5 +10 +10
        # 20 => x
        
