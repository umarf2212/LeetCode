class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        # 'MDCCCLXXXVI'
        # MCMLXXXVI
        i = 0
        Sum = 0
        while i != len(s):
            
            if i == len(s) - 1:
                Sum += nums[s[i]]
                break
            
            if nums[s[i]] >= nums[s[i+1]]:
                Sum += nums[s[i]]
                i += 1
            
            elif nums[s[i]] < nums[s[i+1]]:
                Sum += nums[s[i+1]] - nums[s[i]]
                i+=2
            
            
        
        return Sum
