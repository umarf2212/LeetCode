class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def gcd(a,b):
            if not b:
                return a
            return gcd(b, a%b)
        
        smallest = float('inf')
        largest = float('-inf')
        
        for num in nums:
            if num < smallest:
                smallest = num
            
            if num > largest:
                largest = num
        
        if largest == 1 or smallest == 1: return 1
        
        return gcd(largest, smallest)
