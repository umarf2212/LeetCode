class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        # 2 3 5 6 8 10 15 17

        # We want a+b > c
        # So it makes sense to choose such that a, b < c
        # so that if a+b > c then 
        # (a+1)+b > c and a+(b+1) > c
        # Hence we sort the array
        
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            j = i+1
            for k in range(i+2, len(nums)):
                # we slide j within range i+1 and k until they
                # satisfy a+b <= c => we want a+b > c
                while j < k and nums[i]+nums[j] <= nums[k]:
                    j += 1
                
                # it could be that there are some numbers between j and k
                # but since i+j > k, then i+(j+1) > k so we stop.
                # Count of the numbers between j and k is :
                # k-j => k exclusive or range [j,k)
                count += k-j

        return count
