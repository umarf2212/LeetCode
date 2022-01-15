class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle and not haystack: return 0
        if not needle and haystack: return 0
        
        """
            h -> hlueluilo
            n -> uil
        """
        
        # for h in range(len(haystack)):
#         h = 0
#         n = 0
#         while h < len(haystack):
#             if haystack[h] == needle[n]:
                
#                 n+=1
                
#                 if n == len(needle):
            
#                     return h - len(needle) + 1
#             else:
#                 h = h-n
#                 n = 0
            
#             h += 1
                
        
        return haystack.find(needle)
