class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            j = i+1
            k = len(nums)-1

            while j < k:

                # 1 2 3 3 3 3 4

                Sum = nums[i]+nums[j]+nums[k]

                if Sum == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j+=1

                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                
                elif Sum > 0:
                    k -= 1
                else:
                    j += 1
        
        return res


