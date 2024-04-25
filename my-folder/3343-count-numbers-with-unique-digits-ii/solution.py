from collections import Counter
class Solution:
    def numberCount(self, a: int, b: int) -> int:
        
        return sum([ 1 if len(set([i for i in str(num)])) == len(str(num)) else 0 for num in range(a, b+1) ])
