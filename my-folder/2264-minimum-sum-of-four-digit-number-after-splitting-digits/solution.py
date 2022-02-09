class Solution:
    def minimumSum(self, num: int) -> int:
        
        ar = [int(i) for i in str(num)]
        ar.sort()
        
        return int(str(ar[0])+str(ar[3])) + int(str(ar[1])+str(ar[2]))
