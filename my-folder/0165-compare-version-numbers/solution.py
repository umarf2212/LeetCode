class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split('.')
        v2 = version2.split('.')

        def removeLeadingZeroes(rev):
            leading = True
            res = ''
            for i in range(len(rev)):
                if rev[i] == '0' and leading:
                    continue
                
                elif rev[i] != '0':
                    leading = False

                res += rev[i]
            
            if leading == True:
                return '0'
            
            return res
                


        if len(v1) > len(v2):
            v2 += ['0' for _ in range(len(v1)-len(v2))]
        
        elif len(v2) > len(v1):
            v1 += ['0' for _ in range(len(v2)-len(v1))]
        

        v1 = int(''.join([removeLeadingZeroes(rev) for rev in v1]))
        v2 = int(''.join([removeLeadingZeroes(rev) for rev in v2]))

        print(v1, v2)


        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1

        return 0
