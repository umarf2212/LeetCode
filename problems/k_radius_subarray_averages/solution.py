class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2*k+1: return [-1] * len(nums)

        # 0 1 2 3 4 5 6 7 8 9 10 11 12
        # k = 3


        # p = i-k-1
        # q = i
        # r = i+k+1

        res = [-1] * k
        curSum = sum(nums[:2*k+1])
        res.append(curSum//(2*k+1))
        for i in range(k+1, len(nums)-k):

            p = i-k-1
            q = i
            r = i+k

            curSum -= nums[p]
            curSum += nums[r]

            print(curSum, p, q, r)

            res.append(curSum//(2*k+1))
        
        res += [-1]*k

        return res