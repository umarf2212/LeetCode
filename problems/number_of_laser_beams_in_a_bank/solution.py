class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        def countDevices(s):
            c=0
            for i in s:
                if i == '1':
                    c+=1
            
            return c
        
        
        prevDevicesCount = countDevices(bank[0])
        res = 0
        for i in range(1, len(bank)):
            currDevicesCount = countDevices(bank[i])
            
            if currDevicesCount != 0:
                res += prevDevicesCount * currDevicesCount
                prevDevicesCount = currDevicesCount
        
        return res