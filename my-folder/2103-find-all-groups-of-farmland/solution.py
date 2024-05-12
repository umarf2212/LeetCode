class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        # 1. Traverse the matrix row-wise so that we always find 
        #    the top-left corner of any rectangle.

        # 2. Do DFS on every 1, marking it as visited along the way.
        # 3. The bottom-left corner of any rectangle will have the largest 
        #    i, j values in its 1's coordinates.
        
        m, n = len(land), len(land[0])

        def dfs(i, j, corners):
            if i < 0 or i >= m or j < 0 or j >= n or land[i][j] == 0:
                return

            # currently at [i, j] cell

            # update max i, j coords
            corners[2] = max(corners[2], i)
            corners[3] = max(corners[3], j)            
            
            # mark current cell as visited
            land[i][j] = 0

            # visited rest of the cells within current rectangle
            dfs(i+1, j, corners)
            dfs(i-1, j, corners) 
            dfs(i, j+1, corners)
            dfs(i, j-1, corners)



        # [r1, c1, r2, c2]
        res = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    corners = [i, j, -1, -1]
                    dfs(i, j, corners)

                    if corners[2] == -1 and corners[3] == -1:
                        corners[2], corners[3] = corners[0], corners[1]
                    
                    res.append(corners[:])
        
        return res

        '''
        1 1 0 0 0 1
        1 1 0 0 0 0
        '''
