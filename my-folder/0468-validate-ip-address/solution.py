class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def checkDigits(s):
            if len(s) == 0: return False
            for ch in s:
                if ord(ch) < 48 or ord(ch) > 57:
                    return False
            return True
        
        def checkIPv4(ip):
            if ip[0][0] == '0':
                return False

            for num in ip:
                if not checkDigits(num):
                    return False

                if int(num) < 0 or int(num) > 255:
                    return False
                
                if num[0] == '0' and len(num) > 1: 
                    return False

            return True
 
        # ord('a') = 97
        # ord('f') = 102
        # ord('A') = 65
        # ord('F') = 70
        # ord('0') = 48
        # ord('9') = 57

        def checkIPv6(ip):
            for adr in ip:
                if len(adr) < 1 or len(adr) > 4:
                    return False
                
                for ch in adr:
                    if (97 <= ord(ch) <= 102) or (65 <= ord(ch) <= 70) or (48 <= ord(ch) <= 57):
                        continue
                    else:
                        return False
            
            return True


        ipv4 = queryIP.split('.')
        ipv6 = queryIP.split(':')
        
        if len(ipv4) == 4 and checkIPv4(ipv4):
            return "IPv4"
        
        elif len(ipv6) == 8 and checkIPv6(ipv6):
            return "IPv6"
        
        return "Neither"
