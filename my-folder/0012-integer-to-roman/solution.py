class Solution:
    def intToRoman(self, num: int) -> str:

        d = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        res = ''
        nums = list(d.keys())
        while num > 0:

            for i in range(len(nums)):
                if num < nums[i]:
                    i-=1
                    break

            dm = divmod(num, nums[i])

            if dm[1] == 0:
                res += d[nums[i]] * dm[0]
                break
            else:
                num = dm[1]
                res += d[nums[i]] * dm[0]
        
        return res

