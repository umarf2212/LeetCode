class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if len(box) == len(box[0]) == 1: return box
        # rows -> m
        # cols -> n
        
        # ['#', '#', '.', '*', '.', '#', '.']
        # temp -> [[2,3][1,7]]
        # pair = [2,3]
        # count = 2, obs = 3
        # ['.', '#', '#', '*', '.', '.', '#']
        
        ##edge cases
        # ['*', '.', '.', '.', '.', '#', '#']
        # temp = [[0,0],[2, len(row)]] -> [0,0]
        
        for row in box:
            
            ## store stone counts and obstacle position
            temp = []
            count = 0
            for col in range(len(row)):
                if row[col] == '#':
                    count += 1
                
                elif row[col] == '*':
                    temp.append([count, col])
                    count = 0
            
            if count > 0: 
                temp.append([count, len(row)])
            
            ## gravitating the stones
            i = len(row)
            while temp:
                count, obs = temp.pop()
                
                if obs < i:
                    while i != obs:
                        if i != len(row):
                            row[i] = '.'
                        i -= 1
                
                ## place stones
                if i == obs:
                    i -= 1
                    while count != 0:
                        row[i] = '#'
                        count -= 1
                        i -= 1
            
            if i < len(row):
                while i != -1:
                    row[i] = '.'
                    i-=1
                
        res = []
        box = box[::-1]
        for col in range(len(box[0])):
            temp = []
            
            for row in range(len(box)):
                temp.append(box[row][col])
            
            res.append(temp)
        
        return res