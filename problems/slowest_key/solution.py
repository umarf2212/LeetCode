class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        duration = [releaseTimes[0]]
        mx = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i]-releaseTimes[i-1]
            if diff > mx: mx = diff
            duration.append(diff)
        
        mx_char = float('-inf')        
        for c in range(len(keysPressed)):
            if duration[c] == mx and ord(keysPressed[c]) > mx_char:
                mx_char = ord(keysPressed[c])
        

        return chr(mx_char)
        
        
        