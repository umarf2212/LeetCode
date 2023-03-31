class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10: return -1
        MAX = 2**31 - 1
        
        nums = list(map(int, str(n)))
        
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                break
        
        x = i-1
        y = -1
        for j in range(len(nums)-1,i-1,-1):
            if nums[j] > nums[x]:
                y = j
                break
        
        nums[x], nums[y] = nums[y], nums[x]

        x+=1
        nums[x:] = sorted(nums[x:])

        res = int(''.join(map(str, nums)))

        if res <= n or res > MAX:
            return -1
        
        return res