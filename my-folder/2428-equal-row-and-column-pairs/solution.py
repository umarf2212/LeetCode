class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows = {}
        for row in grid:
            row = tuple(row)
            if row not in rows:
                rows[row] = 0
            rows[row] += 1
        
        cols = {}
        for j in range(len(grid[0])):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][j])

            col = tuple(col)
            if col not in cols:
                cols[col] = 0
            cols[col] += 1
        
        pairs = 0
        for row, count in rows.items():
            if row in cols:
                pairs += count * cols[row]

        return pairs
