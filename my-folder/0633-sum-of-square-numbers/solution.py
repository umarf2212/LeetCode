class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        ar = [i*i for i in range(int(c**(1/2))+1)]
        curSum = 0
        i = 0
        j = len(ar)-1
        while i <= j:
            curSum = ar[i] + ar[j]

            if curSum == c:
                return True

            if curSum > c:
                j-=1
            else:
                i+=1
        
        return False

        # 1 2 3 4 5 6 7 8 9

