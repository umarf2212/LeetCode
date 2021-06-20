class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        d = {}
        
        for i in range(len(secret)):
            if secret[i] in d:
                d[secret[i]].add(i)
            else:
                d[secret[i]] = set([i])
        
        bulls = 0
        bullsPos = deque()
        for i in range(len(guess)):
            if guess[i] in d:
                
                if i in d[guess[i]]:
                    bulls += 1
                    bullsPos.append(i)
                    d[guess[i]].remove(i)
        
        
        cows = 0
        for i in range(len(guess)):
            if bullsPos and i == bullsPos[0]:
                bullsPos.popleft()
            elif guess[i] in d and len(d[guess[i]]) > 0:
                cows += 1
                d[guess[i]].pop()
                if len(d[guess[i]]) == 0:
                    del d[guess[i]]
        
        # print(bulls, cows)
        return str(bulls)+'A'+str(cows)+'B'
