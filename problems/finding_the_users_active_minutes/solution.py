class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        d = {}
        for log in logs:
            if log[0] not in d:
                d[log[0]] = set([log[1]])
            else:
                d[log[0]].add(log[1])
        
        
        
        uamCount = {}
        maxUam = float('-inf')
        for user, minutes in d.items():
            minutes = len(minutes)
            maxUam = max(maxUam, minutes)
            
            if minutes not in uamCount:
                uamCount[minutes] = 1
            else:
                uamCount[minutes] += 1
        
        # print(d, uamCount, maxUam)
        
        ar = [0 for _ in range(k)]
        for uam, userCount in uamCount.items():
            ar[uam-1] = userCount
        
        return ar